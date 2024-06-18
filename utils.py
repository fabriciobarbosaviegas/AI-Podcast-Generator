import re

def writeScript(topic, recast, links):
   topic = normaliseStr(topic)
   fileName = f"scripts/script-{topic.replace(' ', '-')}.txt"
   links = '\n'.join([i['link'] for i in links])
   try:
      file = open(fileName, 'r+')
      file.writelines(f"{topic}:\n\n{recast}\n\n========================================================================================================\n\nArticles:\n\n{links}")
   except FileNotFoundError:
      file = open(fileName, 'w+', encoding='utf-8')
      file.writelines(f"{topic}:\n\n{recast}\n\n========================================================================================================\n\nArticles:\n\n{links}")

   file.close()

   return recast



def normaliseStr(str):
   return str.translate ({ord(c): "" for c in "!@#$%^&*()[]{};:,./<>?\n`~-=_+"})



def num_sort(str):
    return list(map(int, re.findall(r'\d+', str)))[0]
