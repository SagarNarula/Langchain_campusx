from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage 
load_dotenv()

llm=HuggingFacePipeline.from_model_id(model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                                      task="text-generation",
                                      pipeline_kwargs=dict(
                                          temperature=0
                                          )
)

model=ChatHuggingFace(llm=llm)
chat_history=[
    SystemMessage(content='You are a helpful AI assistant')
]  ### To store all the conversation between user and llm.

#model=ChatOpenAI()

while True:
    user_input=input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input=="exit":
        break
    result=model.invoke(chat_history)   #### passing the complete chat_history to the llm to remember previous context.
    chat_history.append(AIMessage(content=result.content))
    print("AI:",result.content)

print(chat_history)
