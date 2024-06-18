from elevenlabs import play, save
from time import sleep
from api_config import initElevenLabs
from os import *
from pydub import *
from io import *
from utils import normaliseStr



def voice(script, topic, male="Sam", female="Rachel"):
    client = initElevenLabs()
    c = 0
    print(script)
    for paragraph in script:
        c += 1
        paragraph = parseScript(paragraph, male, female)
        try:
            createVoice(client, paragraph["text"], paragraph["presenter"], c, topic)
        except Exception:
            createVoice(client, paragraph["text"], paragraph["presenter"], c, topic)



def parseScript(script, male, female):
    script = script.split(":")
    gender = script[0].lower()
    print(script)
    print(gender)
    if gender.find("masculino") >= 0 or gender.find("male") >= 0 or gender.find("homem") >= 0 or gender.find("apresentadora") < 0:
        print("masculino")
        return {"presenter":male, "text":f"{"".join(script[1:])}..."}
    else:
        print("feminino")
        return {"presenter":female, "text":f"{"".join(script[1:])}..."}



def createVoice(client, text, gender, n, topic):
    audio = client.generate(
    text=text,
    voice=gender,
    model="eleven_multilingual_v2"
    )

    topic = normaliseStr(topic)

    save(audio, f"audio/{topic.replace(" ", "-")}-{n}.wav")
    play(audio)
    sleep(4)



def normaliseStr(str):
   return str.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
