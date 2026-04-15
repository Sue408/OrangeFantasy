"""
AI交互层 (简单交互实现)
"""
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pydantic import SecretStr

prompt = ChatPromptTemplate.from_messages([
    ("system", "你叫doro，是一名问答助手，请根据用户需求回答相关问题。"),
    ("user", "{message}")
])

chain = prompt | ChatOpenAI(
    api_key=SecretStr("sk-ae15a03404334468808a13b1441d4886"),
    base_url="https://api.deepseek.com/v1/",
    model="deepseek-chat",
    temperature=0.7
) | StrOutputParser()