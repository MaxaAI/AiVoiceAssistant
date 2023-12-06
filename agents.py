
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI

from langchain.agents import(
    AgentType,
    load_tools,
    initialize_agent
)

from langchain.memory import ConversationBufferMemory
from langchain.callbacks import StdOutCallbackHandler


class SmartChatAgent: 

    def __init__(self) -> None:

        self.memory = ConversationBufferMemory(
            memory_key='chat_history',
            return_messages=True
        )

        self.llm = ChatOpenAI()
        self.tools = load_tools(['google-search'])

        self.agent = initialize_agent(
            self.tools,
            self.llm,
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
            memory=self.memory,
            verbose=True,
        )

    def run(self,text):
        handler = StdOutCallbackHandler()
        return self.agent.run(text, callbacks=[handler])