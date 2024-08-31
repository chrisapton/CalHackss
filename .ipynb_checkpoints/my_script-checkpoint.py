import pandas as pd
import numpy as np
from llama_index import VectorStoreIndex, Document, SimpleDirectoryReader
import os
from pathlib import Path
from llama_index import download_loader
from llama_index.llms import OpenAI
from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext

def some_function(input_text):
    # export OPENAI_API_KEY=
    api_key = os.environ.get('OPENAI_API_KEY')
    # os.environ['OPENAI_API_KEY'] =
    
    # Choose between chat gpt 4 or 3.5
    #llm = OpenAI(temperature=0.1, model="gpt-4")
    llm = OpenAI(temperature=0.1)
    llm.max_tokens=1000
    service_context = ServiceContext.from_defaults(llm=llm)


    # Convert PDF to text

    PDFReader = download_loader("PDFReader")

    loader = PDFReader()
    documents = loader.load_data(file=Path('./temp.pdf'))

    # Construct a simple vector index
    index = VectorStoreIndex(documents, service_context=service_context)

    # Save your index to a index.json file
    # index.storage_context.persist(persist_dir="index.json")
    print(index)
    query_engine = index.as_query_engine()
    response = query_engine.query("Make this question very verbose." + input_text)
    return response



