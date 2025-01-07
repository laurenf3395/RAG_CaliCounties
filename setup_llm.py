import getpass
import os
#print(os.environ)
os.environ["NVIDIA_API_KEY"] = getpass.getpass()

from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings


def setup_llm():
    llm = ChatNVIDIA(
        model="meta/llama-3.1-70b-instruct",
        api_key="", # ADD API Key from NVIDIA AI Foundation models for LLMs
        temperature=0.2,
        top_p=0.7,
        max_tokens=1024)
    return llm

def setup_embeddings():
    embeddings = NVIDIAEmbeddings(model="nvidia/nv-embedqa-e5-v5", api_key="", truncate="NONE") # ADD API Key from NVIDIA AI Foundation models for embedding models

    return embeddings


