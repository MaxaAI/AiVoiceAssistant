from dotenv import load_dotenv

load_dotenv()

from interface import AudioInterface
from agents import SmartChatAgent

interface = AudioInterface()
agent = SmartChatAgent()

while True:
    text = interface.listen()
    response = agent.run(text)
    interface.speak(response)