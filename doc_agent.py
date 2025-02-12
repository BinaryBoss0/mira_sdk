#!pip install mira-sdk
#!pip install composio_langchain


from mira_sdk import MiraClient
client = MiraClient(config={"API_KEY": "mira_api_keys"})

from dotenv import load_dotenv
from mira_sdk import MiraClient
import os

MIRA_API_KEY="mira_api_keys"

load_dotenv()
client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})

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
    api_key = "your_api_key",
)
prompt = hub.pull("hwchase17/openai-functions-agent")

composio_toolset = ComposioToolSet(api_key="px6xqpbep7510sjdhdii5")
tools = composio_toolset.get_tools(actions=['GOOGLEDOCS_CREATE_DOCUMENT'])

agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

task = "your query Example:(create a google document with name LLM, where document contains applications of LLM)"
result = agent_executor.invoke({"input": task})
print(result)