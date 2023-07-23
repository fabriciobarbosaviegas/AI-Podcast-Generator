from elevenlabs import generate, play, save
from time import sleep



def voice(script, topic, male="Sam", female="Bella"):
    c = 0
    for paragraph in script:
        c += 1
        paragraph = parseScript(paragraph, male, female)
        try:
            createVoice(paragraph["text"], paragraph["presenter"], c, topic)
        except Exception:
            createVoice(paragraph["text"], paragraph["presenter"], c, topic)



def parseScript(script, male, female):
    script = script.split(":")
    gender = script[0].lower()
    if gender.find("masculino") >= 0 or gender.find("male") >= 0 or gender.find("homem") >= 0:
        print("masculino")
        return {"presenter":male, "text":f"{script[1]}..."}
    else:
        print("feminino")
        return {"presenter":female, "text":f"{script[1]}..."}



def createVoice(text, gender, n, topic):
    audio = generate(
    text=text,
    voice=gender,
    model="eleven_multilingual_v1"
    )

    play(audio)
    save(audio, f"audio/{topic}-{n}.mp3")
    sleep(4)
