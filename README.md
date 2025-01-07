# Retrieval-Augmented Generation (RAG) for providing information about California Counties

## Key Components

- Document Processing Pipeline
- Vector Embeddings Generation
- Query Processing System
- Response Generation Framework

## Steps to Setup the Retrieval-Augmented Generation (RAG)

1. Download Wikipedia pages of California Counties
Run `crawl_wikipages.py` to download wikipedia pages of all the California counties. Setup up the download folder in `dir_` in the code.

2. Load database from folder after download
`setup_db.py` will setup the database and populate the FAISS DB of the text files downloaded using DirectoryLoader

3. Text Splitting
Split text into chunks using RecursiveCharacterTextSplitter, which will recursively split the document using common separators like new lines until each chunk is the appropriate size. This is the recommended text splitter for generic text use cases.

4. Setup Chat Model
Using NVIDIA AI Foundation models from https://build.nvidia.com/meta/llama-3_1-70b-instruct?snippet_tab=Python (follow instructions here https://python.langchain.com/docs/integrations/chat/nvidia_ai_endpoints/)

Setup NVIDIA_API_KEY as environment variable: 
`echo "export NVIDIA_API_KEY='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'" >> ~/.zshrc`

`source ~/.zshrc` 

`echo $NVIDIA_API_KEY`

Also setup API keys in `setup_llm.py` from build.nvidia.com

5. Choosing a vector database and choosing an index

Vector databases: Based on size of dataset(~12000 characters), using a simple lightweight vector db makes sense: such as FAISS, ChromaDB, PineCone.
Selected: FAISS

Choosing an index in FAISS
### **How to Select the Right FAISS Index**

| **Requirement** | **Recommended Index** | **Comments** |
| --- | --- | --- |
| Small dataset (exact search) | `IndexFlatL2` or `IndexFlatIP` | Fast and simple. |
| Medium dataset (speed-focused) | `IndexIVFFlat` or `IndexHNSWFlat` | Balance between speed and accuracy. |
| Large dataset (memory-focused) | `IndexIVFPQ` | Memory-efficient, approximate. |
| GPU Acceleration | GPU version of any index | Faster searches with GPU. |

6. Running the RAG

Once all the API keys are set, run `rag_application.py` and ask your LLM any question about California Counties you may want to know about!

