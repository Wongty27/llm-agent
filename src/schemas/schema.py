from pydantic import BaseModel, Field
from typing import Annotated
class Citation(BaseModel):
    file_name: str = Field(..., min_length=1)
    page_number: int = Field(..., gt=0)
    paragraph: str = Field(..., min_length=1)

class UserProfile(BaseModel):
    user_name: str = Field(..., min_length=1)

class SQLQuery(BaseModel):
    query: Annotated[str]
    explanation: str = Field("", description="Explanation of the SQL query.")

