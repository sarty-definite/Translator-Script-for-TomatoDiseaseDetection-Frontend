from googletrans import Translator
import json

with open("tomatoLeafData.txt", 'r', encoding='utf-8') as file:
    tomatoLeafData = eval(file.read())

translator = Translator(service_urls=['translate.googleapis.com'])

code = {'English':'en', 'Hindi':'hi', 'Tamil':'ta', 'Bengali':'bn'}
languages = ['Hindi', 'Tamil', 'Bengali']
keys = ['generalInfo', 'visualCues', 'prevention', 'cure']

for disease in tomatoLeafData:
    for language in languages:
        for key in keys:
            tomatoLeafData[disease][language][key] = str(translator.translate(tomatoLeafData[disease]['English'][key], dest=code[language]).text)

with open("tomatoLeafData.json", 'w', encoding='utf-8') as file:
    file.write(json.dumps(tomatoLeafData, ensure_ascii=False, indent=4))