from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import gradio as gr

# initialize the models
openai = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key="your api key"
)
def chatbot(prompt):
    # Template untuk langkah demi langkah
    template = f"Cara langkah demi langkah: {prompt}\n"
    return openai.invoke(template).content

interface = gr.Interface(fn=chatbot, inputs="text", outputs="text")
interface.launch(share=True)