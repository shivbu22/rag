from langchain_community.document_loaders import WebBaseLoader
data = WebBaseLoader("https://www.apple.com/in/shop/buy-iphone/iphone-17-pro")

data = data.load()
print(data[0].page_content)