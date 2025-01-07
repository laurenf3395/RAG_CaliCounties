#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module sets up and populates the vector database FAISS 
with the wikipedia pages of California counties

"""
import faiss
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore

from setup_llm import setup_embeddings

def load_db(data_path):

    # loading documents
    loader = DirectoryLoader(data_path, glob="**/*.txt", show_progress=True)
    docs = loader.load()

    print(f"Total characters: {len(docs[0].page_content)}")

    # Split documents into chunks to fit into context window
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  # chunk size (characters)
        chunk_overlap=200,  # chunk overlap (characters)
        add_start_index=True,  # track index in original document
    )
    all_splits = text_splitter.split_documents(docs)

    print(f"Split 58 wiki pages into {len(all_splits)} sub-documents.")

    # Setup chat model
    embeddings = setup_embeddings()

    # Setup Vector database and store documents
    # Create Index
    #print("EMB", embeddings)
    index = faiss.IndexFlatL2(1024) # Dimension of embeddings = 1024 : nv model

    vector_db = FAISS(index=index, embedding_function=embeddings, \
                    docstore=InMemoryDocstore(), index_to_docstore_id={})

    document_ids = vector_db.add_documents(documents=all_splits)

    print(len(document_ids))

    return vector_db

if __name__ == "__main__":

    path_to_data = "data_counties"
    load_db(path_to_data)






