from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()

template = ChatPromptTemplate.from_template("You are a helpful assistant that translates {English} to {Hindi}.")
data = PyPDFLoader("document loaders/deeplearning.pdf")
prompt = template.format_prompt(English="Hello", Hindi="नमस्ते")
model = ChatMistralAI(model_name="mistral-small-2506")
result =model.invoke(prompt)
print(result.content)