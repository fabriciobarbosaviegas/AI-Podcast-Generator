from robots.search import search
from robots.accurate import accurate
from robots.recast import recast
from robots.editor import editor
from robots.translate import translate
from robots.voice import voice
from robots.podcast import merge_audios
from api_config import initChatGptAPI
from utils import *
from time import sleep
import simple_colors  



def main():
   initChatGptAPI()

   topic = input("topic: ")

   print(simple_colors.blue("\n\nsearch:\n"))
   searchResults = search(topic)

   print(simple_colors.yellow("\n\naccurate:\n\n"))
   articles = accurate(topic, searchResults)
   print(articles)
   
   comments = ''

   for i in range(3):
      print(simple_colors.green("\n\nrecast:\n\n"))
      recasted = recast(topic, articles, comments)
      sleep(3)

      print(simple_colors.magenta("\n\neditor:\n\n"))
      comments = editor(recasted) + "\nLeve meus comentários em consideração, mas devolva um podcast, você não deve incluir nenhuma resposta dirigida a mim em sua história"
      sleep(3)

   recasted = writeScript(topic, recast(topic, articles, comments), articles)

   voice(translate(recasted).split("\n\n"), topic, female="Gigi")
   
   merge_audios('audio', normaliseStr(topic))

   while True:
      close = int(input('Write 0 to close the program: '))
      if close == 0:
         break



if __name__ == "__main__":
   main()
