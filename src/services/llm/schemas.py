from pydantic import BaseModel, Field

class QueryOutput(BaseModel):
    """Schema of generated SQL query."""

    query: str = Field(..., description="Generated SQL query.")