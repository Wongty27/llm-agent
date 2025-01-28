import os
from datetime import date
from typing import TypedDict
from pydantic_ai import Agent, ModelRetry, RunContext

class ResultType(TypedDict):
    """
    Never coerce data to this type.
    """

ANTHROPIC_KEY = os.getenv("GEMINI_API_KEY")

sql_agent = Agent(
    model="google-gla:gemini-1.5-flash",
    result_type=str,
    system_prompt="Use the user's name while replying to them.",
    model_settings={
        "temperature": 0.0,
        "max_tokens": 100,
    }
)

@sql_agent.system_prompt
async def add_user_name(ctx: RunContext[str]) -> str:
    return f"The user's name is {ctx.deps}"

# @sql_agent.system_prompt
# def add_the_date() -> str:  
#     return f'The date is {date.today()}.'

@sql_agent.tool
async def get_weather(location: str) -> str:
    return f"Today in {location} the weather is sunny"

@sql_agent.tool_plain(retries=5)
def infinite_retry_tool() -> int:
    raise ModelRetry("Please retry again.")

@sql_agent.tool(retries=3)
async def get_sql_query(ctx: RunContext[str]) -> str:
    return f"SELECT * FROM {ctx.deps}"
