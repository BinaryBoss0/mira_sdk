#!/usr/bin/env python
# coding: utf-8

#!pip install mira-sdk
#!pip install composio_langchain



from mira_sdk import MiraClient
client = MiraClient(config={"API_KEY": "your_mira_api_key"})

MIRA_API_KEY="your_mira_api_key"   #create your own free mira api key

from dotenv import load_dotenv
import os
load_dotenv()
client = MiraClient(config={"API_KEY": os.getenv("your_mira_api_key")})


from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain import hub
from langchain_openai import ChatOpenAI
from composio_langchain import ComposioToolSet, Action, App

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key = "your_model_key",
)

prompt = hub.pull("hwchase17/openai-functions-agent")

composio_toolset = ComposioToolSet(api_key="px6xqpbep7510sjdhdii5")
tools = composio_toolset.get_tools(actions=['GOOGLECALENDAR_CREATE_EVENT'])

agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

task = "your request Example:create a event name LLM, at 1:00 PM on 13 Feb,2025 Indian Standard Time,also send invitation to ashu on abc@gmail.com"
result = agent_executor.invoke({"input": task})
print(result)



