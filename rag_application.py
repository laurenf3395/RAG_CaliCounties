from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from typing_extensions import List, TypedDict

from setup_llm import setup_llm
from setup_db import load_db


prompt = ChatPromptTemplate.from_messages([
        ("human", "You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. \
         If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise. \
         Question: {question} \
         Context: {context} \
         Answer:")])

llm = setup_llm()
vector_store = load_db("data_counties")

question = input("Hey! What would you want to ask me regarding California Counties?")

retrieved_docs = vector_store.similarity_search(question)
docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)
prompt = prompt.invoke({"question": question, "context": docs_content})
answer = llm.invoke(prompt)

print(answer['content'])