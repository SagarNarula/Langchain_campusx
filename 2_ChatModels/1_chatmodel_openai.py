from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model="gpt-4")

result=model.invoke("What is the capital of India?")
print(result) ### This will fetch the complete details
print(result.content)  ### This will fetch the content.


model=ChatOpenAI(model="gpt-4",temperature=0,max_completion_tokens=10)
result=model.invoke("Suggest me 5 indian male names")
print(result.content)
