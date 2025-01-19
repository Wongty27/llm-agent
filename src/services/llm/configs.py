import os
from typing import Literal
from dotenv import load_dotenv
from pymongo import MongoClient
from databases.postgres_db import engine
from langchain_core.globals import set_llm_cache
from langchain_community.cache import InMemoryCache
from langchain_google_genai.llms import GoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters.character import CharacterTextSplitter

client = MongoClient("")

load_dotenv("../.env")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GEMINI_API_KEY)
llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key=GEMINI_API_KEY, temperature=0)

set_llm_cache(InMemoryCache())

sql_toolkit = SQLDatabaseToolkit(db=SQLDatabase(engine), llm=llm)

def get_vector_store(
    vector_db_name: str,
    collection_name: str,
    index_name: str,
    ):
    vector_store = MongoDBAtlasVectorSearch(
        collection=client[vector_db_name][collection_name],
        embedding=embeddings,
        index_name=index_name
    )
    vector_store._index_name
    vector_store.create_vector_search_index(dimensions=1024)
    return vector_store

def load_documents(
    docs_path: str,
    file_type: Literal["pdf", "docx", "csv"] = "pdf"
):
    doc_loader = DirectoryLoader(docs_path, glob=f"**/*.{file_type}", use_multithreading=True)
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100, add_start_index=True)
    return text_splitter.split_documents(doc_loader.load())