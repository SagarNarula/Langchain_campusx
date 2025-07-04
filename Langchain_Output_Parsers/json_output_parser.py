from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)
parser=JsonOutputParser()

## 1st prompt --> Detailed Report
# template=PromptTemplate(template='Give me the name,age,city of a fictional person \n {format_instruction}',
#                          input_variables=[],
#                          partial_variables={'format_instruction':parser.get_format_instructions()})

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)




#prompt=template.format()

#print(prompt)

# result=model.invoke(prompt)
# final_result=parser.parse(result.content)

chain=template | model |parser

result2=chain.invoke({'topic':"Black Hole"})

print(result2)
#print(final_result)