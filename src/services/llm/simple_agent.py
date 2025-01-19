from langchain import hub
from langgraph.prebuilt import create_react_agent
from configs import llm, sql_toolkit
from services.llm.schemas import QueryOutput
prompt_template = hub.pull("langchain-ai/sql-agent-system-prompt")
system_message = prompt_template.format(dialect="postgres", top_k=3)

agent_executor = create_react_agent(
    model=llm,
    tools=sql_toolkit.get_tools(),
    state_modifier=system_message
)