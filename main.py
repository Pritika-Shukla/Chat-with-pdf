## Chat with memory

from langchain_openai import  ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from langgraph.checkpoint.memory import InMemorySaver  
from langchain.agents import create_agent

agent=create_agent(
    model='gpt-4o-mini',
    checkpointer=InMemorySaver(),  
)
 
thread_config = {"configurable": {"thread_id": "1"}}

print("✅ Live chat started (type 'exit' to stop)\n")

while True:
    user_input=input("You: ")
    if user_input.lower() == "exit":
        break
      
    result=agent.invoke(
         {"messages": [{"role": "user", "content": user_input}]},
        thread_config,
    )
    print("Bot:", result["messages"][-1].content)
    print()