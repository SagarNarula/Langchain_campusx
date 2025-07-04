from langchain_core.prompts import PromptTemplate

## template
template=PromptTemplate(
    template=""" Please summarize the research paper titled "{paper_input}" with following specification:
    Explaination style:{style_input}
    Explaination length:{length_input}""",input_variables=["paper_input","style_input","length_input"]
                        )

template.save('template.json')