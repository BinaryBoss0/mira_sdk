#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install mira-sdk')


# In[2]:


from mira_sdk import MiraClient
client = MiraClient(config={"API_KEY": "sb-8b123378789592cbc25133af1cfeb9f9"})


# In[3]:


MIRA_API_KEY="sb-8b123378789592cbc25133af1cfeb9f9"


# In[4]:


from dotenv import load_dotenv
from mira_sdk import MiraClient
import os

load_dotenv()
client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})


# In[6]:


#!pip install composio_langchain


# In[5]:


from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain import hub
from langchain_openai import ChatOpenAI
from composio_langchain import ComposioToolSet, Action, App


# In[11]:


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key = "sb-8b123378789592cbc25133af1cfeb9f9",
)


# In[9]:


prompt = hub.pull("hwchase17/openai-functions-agent")

composio_toolset = ComposioToolSet(api_key="px6xqpbep7510sjdhdii5")
tools = composio_toolset.get_tools(actions=['GMAIL_SEND_EMAIL'])

agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


# In[13]:


task = "send a mail to suhail@iiitd.ac.in , with subject lunch?, ask suhail if he wanna join me a lunch at 12:30pm"
result = agent_executor.invoke({"input": task})
print(result)


# In[ ]:




