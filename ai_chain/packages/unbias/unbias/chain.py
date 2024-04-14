from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv
import os 

load_dotenv()
print(os.environ)

template = """Answer the question based only on the following context:


Comment: {comment}
"""
prompt = ChatPromptTemplate.from_template(template)

# LLM
from langchain_anthropic import ChatAnthropic
model = ChatAnthropic(model='claude-3-opus-20240229')





# RAG chain
chain = (
    RunnableParallel({"comment": RunnablePassthrough()})
    | prompt
    | model
    | StrOutputParser()
)


# Add typing for input
class Comment(BaseModel):
    __root__: str


chain = chain.with_types(input_type=Comment)
