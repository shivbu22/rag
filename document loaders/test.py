from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader("document loaders/GRU.pdf")
data = data.load()
print(data)