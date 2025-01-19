import os
from datetime import date
from typing import TypedDict
from pydantic_ai import Agent, ModelRetry, RunContext

class ResultType(TypedDict):
    """
    Never coerce data to this type.
    """



ANTHROPIC_KEY = os.getenv("ANTHROPIC_KEY")

agent = Agent(
    model="claude-3-5-sonnet-latest",
    result_type=str,
    system_prompt="Use the user's name while replying to them.",
    model_settings={
        "temperature": 0.0,
        "max_tokens": 100,
    }
)

@agent.system_prompt
async def add_user_name(ctx: RunContext[str]) -> str:
    return f"The user's name is {ctx.deps}"

@agent.system_prompt
def add_the_date() -> str:  
    return f'The date is {date.today()}.'

@agent.tool
async def get_weather(location: str) -> str:
    return f"Today in {location} the weather is sunny"

@agent.tool_plain(retries=5)
def infinite_retry_tool() -> int:
    raise ModelRetry("Please retry again.")

@agent.tool(retries=3)
async def get_sql_query(ctx: RunContext[str]) -> str:
    return f"SELECT * FROM {ctx.deps}"
