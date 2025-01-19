from fastapi import APIRouter
from services.llm.configs import get_vector_store, load_documents
from services.llm.simple_agent import agent_executor
router = APIRouter(
    prefix="/llm",
    tags=["llm"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
# async def create_vector_store():
#     vector_store = get_vector_store(
#         vector_db_name="GEMINI",
#         collection_name="References",
#         index_name="References"
#     )
#     return vector_store

@router.get("/")
async def get_sql_query(user_query: str):
    events = agent_executor.stream(
        {"messages": [("user", user_query)]},
        stream_mode="values"
    )
    for event in events:
        event["messages"][-1].pretty_print()

@router.get("/")
async def get_citation(user_query: str):
    """
    Get source, page, and page_content.
    """
    retriever = get_vector_store(
        vector_db_name="GEMINI",
        collection_name="References",
        index_name="References"
    ).as_retriever(search_kwargs={"k": 3})
    response = retriever.invoke(user_query)
    return response

@router.post("/")
async def add_documents(documents_path: str):
    doc_splits = load_documents(docs_path=documents_path)
    vector_store = get_vector_store(
        vector_db_name="GEMINI",
        collection_name="References",
        index_name="References"
    )
    vector_store.add_documents(documents=doc_splits)

@router.delete("/")
async def delete_documents():
    vector_store = get_vector_store(
        vector_db_name="GEMINI",
        collection_name="References",
        index_name="References"
    )
    vector_store.delete(ids=)

@router.get("/")
async def get_vector_search(user_query: str):
    vector_store = get_vector_store(
        vector_db_name="GEMINI",
        collection_name="References",
        index_name="References"
    )
    responses = vector_store.similarity_search(query=user_query, k=3)
    for res in responses:
        return res.page_content, res.metadata