import os
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_community.embeddings import OllamaEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda,RunnablePassthrough,RunnableParallel

load_dotenv()

llm=ChatGroq(model="Gemma2-9b-It")

def create_embeddings(video_id):
    try:
    # If you don’t care which language, this returns the “best” one
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])

    # Flatten it to plain text
        transcript = " ".join(chunk["text"] for chunk in transcript_list)
        #print(transcript)

    except TranscriptsDisabled:
        print("No captions available for this video.")
    text_splitters=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    chunks=text_splitters.create_documents([transcript])
    embeddings=OllamaEmbeddings(model="mxbai-embed-large")
    vectorstore=FAISS.from_documents(chunks,embeddings)
    retriever=vectorstore.as_retriever(search_type="similarity",search_kwargs={'k':4})
    return retriever


def format_docs(retrieved_docs):
    context_text="\n\n".join(doc.page_content for doc in retrieved_docs)
    return context_text

def generate_response(user_input,retriever):
    parallel_chain=RunnableParallel({
    'context':retriever|RunnableLambda(format_docs),
    'question':RunnablePassthrough()
    })
    parser=StrOutputParser()

    main_chain=parallel_chain|user_input|llm|parser

    response=main_chain.invoke(user_input)
    return response
    

    

### Title of the App
st.title("RAG Application")

### side bar for settings:
st.sidebar.title("Settings")
video_id=st.sidebar.text_input("Enter the youtube video id:")

if video_id:
    retriever=create_embeddings(video_id)
    st.sidebar.write("Vector Database is ready")

### Main interface for user input:
st.write("Go ahead ask your questions")
user_input=st.text_input("You:")
if user_input:
    response=generate_response(user_input,retriever)
    st.write(response)


