from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel,RunnableSequence,RunnablePassthrough,RunnableLambda,RunnableBranch


load_dotenv()

def word_count(text):
    return len(text.split())

prompt=PromptTemplate(template="Write a detailed report on {topic}",
                      input_variables=['topic'])

prompt2=PromptTemplate('Summarize the following text {text}',
                       input_variables=['text'])

model=ChatOpenAI()

parser=StrOutputParser()

report_gen_chain=RunnableSequence(prompt,model,parser)

branch_chain=RunnableBranch(
    (lambda x:len(x.split())>500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain=RunnableSequence(report_gen_chain,branch_chain)
result=final_chain.invoke({'topic':'Russia vs Ukraine'})

print(result)