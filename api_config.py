import openai
from elevenlabs.client import ElevenLabs



def initChatGptAPI():
    openai.api_key = 'API_KEY'
    return openai



def initElevenLabs():
    client = ElevenLabs(api_key="API_KEY")
    return client

def setBraveAPI():
    return 'API_KEY'
