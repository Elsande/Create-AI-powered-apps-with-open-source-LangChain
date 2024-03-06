from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
import wget
import os
import gradio as gr
import pysqlite3
import sys

sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

loader = TextLoader('text.txt')

openai_api_key = "your api key"
os.environ["OPENAI_API_KEY"] = openai_api_key

# mengakses data
data = loader.load()

# Membuat instance untuk mencari data
index = VectorstoreIndexCreator().from_loaders([loader])

# Menjalankan gradio
def summarize(query):
    return index.query(query)

iface = gr.Interface(fn=summarize, inputs="text", outputs="text")
iface.launch(share=True)