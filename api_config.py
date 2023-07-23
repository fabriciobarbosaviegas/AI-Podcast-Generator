import openai
from elevenlabs import set_api_key



def initChatGptAPI():
    openai.api_key = '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'
    return openai



def initElevenLabs():
    set_api_key('c156313da25c8807863fb1587dcd2421')



def setBraveAPI():
    return 'BSAVoB-xtxycJAzL1Bg0gfGxfQPiWOr'