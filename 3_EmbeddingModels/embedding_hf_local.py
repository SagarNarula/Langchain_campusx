from langchain_huggingface import HuggingFaceEmbeddings


embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text="Delhi is the capital of India"

documents=[
    "Delhi is the capital of India",
    "Kolkata is the capital of WestBengal",
    "Paris is the capital of france"
]

result=embedding.embed_query(text)

result1=embedding.embed_documents(text)

print(str(result1))