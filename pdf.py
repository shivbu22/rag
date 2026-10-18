from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader("document loaders/deeplearning.pdf")
loader = data.load()
print(len(loader))  
print(loader[14])