from fastapi import APIRouter
from services.agents import agent
from pydantic_ai.exceptions import UsageLimitExceeded
from pydantic_ai.settings import UsageLimits

router = APIRouter(
    prefix="/weather",
    tags=["Weather"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_weather(query: str) -> str:
    try:
        agent.run_stream(
            user_prompt=query,
            deps="",
            usage_limits=UsageLimits(
                request_limit=3,
                response_tokens_limit=10
            )
        )
    except UsageLimitExceeded as e:
        print(e)