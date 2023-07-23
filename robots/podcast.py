import os
from pydub import AudioSegment



def merge_audios(path):
    audios = []

    for audio in os.listdir(path):
        if audio.endswith(".wav"):
            audios.append(AudioSegment.from_mp3(f"{path}/{audio}"))

    combined = audios[0]

    for i in audios[1:]:
        combined += i

    combined.export(f"{path}/final.mp3", format="mp3")