from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
loader=DirectoryLoader(
    path="Books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs=loader.load()

#docs=loader.lazy_load()

print(len(docs))

for document in docs:
    print(document.metadata)


# print(docs[0].page_content)
# print(docs[0].metadata)

