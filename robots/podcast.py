import os
from utils import num_sort
from pydub import AudioSegment



def merge_audios(path, name="final"):
    audios = []
    files = os.listdir(path)
    files.sort(key=num_sort)
    print(files) 

    for audio in files:
        print(f"{path}/{audio}")
        if audio.endswith(".wav"):
            audios.append(AudioSegment.from_mp3(f"{path}/{audio}"))

    combined = audios[0]

    for i in audios[1:]:
        combined += i

    combined.export(f"{path}/{name}.mp3", format="mp3")

    deleteTrashFiles(path, files)



def deleteTrashFiles(path, files):
    for fname in files:
        os.remove(f'{path}/{fname}')
