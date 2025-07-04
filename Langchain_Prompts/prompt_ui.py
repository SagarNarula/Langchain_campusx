from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt

#load_dotenv()

#model=ChatOpenAI()

llm=HuggingFacePipeline.from_model_id(model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                                      task="text-generation",
                                      pipeline_kwargs=dict(
                                          temperature=0
                                          )
)

model=ChatHuggingFace(llm=llm)

st.header("Research Tool")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

## template Creating a template here:
# template=PromptTemplate(
#     template=""" Please summarize the research paper titled "{paper_input}" with following specification:
#     Explaination style:{style_input}
#     Explaination length:{length_input}""",input_variables=["paper_input","style_input","length_input"]
#                         )

### Loading the prompt template from a json file:
template=load_prompt('template.json')
#input_variables=["paper_input","style_input","length_input"]

prompt=template.invoke({"paper_input":paper_input,"style_input":style_input,"length_input":length_input})

#user_input=st.text_input("Enter your prompt")  ### Example of Static Prompt

if st.button('Summarize'):
    #result=model.invoke(user_input)
    result=model.invoke(prompt)
    st.write(result.content)
