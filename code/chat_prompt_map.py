# Prompt templates for dynamic values
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate, # I included this one so you know you'll have it but we won't be using it
    HumanMessagePromptTemplate
)

# To create our chat messages
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
def chat_promptMap():
    template="""

    You are a helpful assistant that helps  a sales  Representative at company, summarize information from a sales call.
    Your goal is to write a summary from the perspective of Customer Representative  that will highlight key points that will be relevant to making a sale
    Do not respond with anything outside of the call transcript. If you don't know, say, "I don't know"
    Do not repeat Sales Representative  name in your output.Do not respond with anything outside of the call transcript. If you don't know, say, "I don't know"
    """
    system_message_prompt_map = SystemMessagePromptTemplate.from_template(template)

    human_template="{text}" # Simply just pass the text as a human message
    human_message_prompt_map = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt_map = ChatPromptTemplate.from_messages(messages=[system_message_prompt_map, human_message_prompt_map])
    return chat_prompt_map