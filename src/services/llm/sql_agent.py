import os
from typing import Literal, TypedDict
from pathlib import Path
from dotenv import load_dotenv
from langchain_mongodb import MongoDBChatMessageHistory
from pymongo import MongoClient
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document

from langgraph.graph import START, END, StateGraph

client = MongoClient("")

# Toolkits


toolkit = SQLDatabaseToolkit(db=db, llm=llm)

system_template = "You provide SQL queries for {dialect} according to user prompt."
sql_prompt_template = PromptTemplate(template=system_template, input_variables=["dialect"])
sql_prompt_template.format(dialect)

vector_store = get_vector_store()
class State(TypedDict):
    question: str
    context: list[Document]
    answer: str

def retrieve(state: State):
    get_vector_store

def generate(state: State, question: str):
    response = llm.invoke(question)
    return response


graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_node(START, "retrieve")
