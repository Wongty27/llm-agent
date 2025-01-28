from fastapi import APIRouter
from pydantic_ai.usage import UsageLimits
from pydantic_ai import exceptions
from services.llm.agents import sql_agent

router = APIRouter(
    prefix="/llm",
    tags=["llm"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def get_data():
    pass

@router.get("/")
async def get_sql_query(user_query: str):
    try:
        async with sql_agent.run_stream(
            user_prompt=user_query,
            usage_limits=UsageLimits(request_limit=1, response_tokens_limit=10)
        ) as response:
            return await response.get_data()
    except exceptions.UsageLimitExceeded as e:
        print(e)

@router.get("/")
async def get_citation(user_query: str):
    """
    Get source, page, and page_content.
    """
    pass

@router.post("/")
async def add_documents(documents_path: str):
    pass

@router.delete("/")
async def delete_documents():
    pass

@router.get("/")
async def get_vector_search(user_query: str):
    pass