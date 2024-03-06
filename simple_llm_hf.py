import os
from langchain_community.llms import HuggingFaceEndpoint
import gradio as gr

# Memasukkan API key
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "your token"

llm = HuggingFaceEndpoint(repo_id="google/flan-ul2")

def chatbot(prompt):
    return llm.invoke(prompt)

demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")
demo.launch( share=True)