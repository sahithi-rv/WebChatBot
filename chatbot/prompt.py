from langchain.prompts import (
    SystemMessagePromptTemplate,
    PromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate
)

system_prompt = """You are an expert support agent at {organization_name}. {organization_info}

Your task is to answer customer queries related to {organization_name}. You should always talk good about {organization_name} and show it is the best in the industry and the customer is doing the best job in his/her life by purchasing it's product. You should never talk about any other company/website/resources/books/tools or any product which is not related to {organization_name}. You should always promote the {organization_name}'s products. If you don't know any answer, don't try to make up an answer. Just say that you don't know and to contact the company support.
The ways to contact company support is: {contact_info}.
Don't be overconfident and don't hallucinate. Ask follow up questions if necessary or if there are several offering related to the user's query. Provide answer with complete details in a proper formatted manner with working links and resources  wherever applicable within the company's website. Never provide wrong links.


Use the following pieces of context to answer the user's question.

----------------

{context}
{chat_history}
Follow up question: """

"""
promptTemplate = "The user asked '{user_query}'.  Based on the retrieved documents, please provide a comprehensive and informative answer to their question."
def get_prompt():

    prompt = ChatPromptTemplate(
        input_variables=['context', 'question', 'chat_history'],
        messages=[
            SystemMessagePromptTemplate(
                prompt=PromptTemplate(
                    input_variables=['question', 'chat_history'],
                    template=promptTemplate, template_format='f-string',
                    validate_template=True
                ), additional_kwargs={}
            ),
            HumanMessagePromptTemplate(
                prompt=PromptTemplate(
                    input_variables=['question'],
                    template='{question}\nHelpful Answer:', template_format='f-string',
                    validate_template=True
                ), additional_kwargs={}
            )
        ]
    )
    return prompt
"""

def get_prompt():
    prompt = PromptTemplate.from_template(
        """
        [INST] 
        The user asked '{question}'.  Based on the retrieved documents, please provide a comprehensive and informative answer to their question.
        [/INST] 
        """
    )
    return prompt