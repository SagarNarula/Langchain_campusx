from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatOpenAI()

## 1st prompt --> Detailed Report
template1=PromptTemplate(template='Write a detailed report on {topic}',
                         input_variables=['topic'])



### 2nd prompt --> Summary
template2=PromptTemplate(template="Write a 5 line summary line on the following text /n {text}",
                         input_variables=['text'])

parser=StrOutputParser()

chain=template1 | model | parser | template2 | model | parser 

result=chain.invoke({'topic':'Black Hole'})

print(result)