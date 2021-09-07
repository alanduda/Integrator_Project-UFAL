import json
import os

def saveJson(data, fileName):
    if not os.path.isdir('results'):
       try:
         os.mkdir('results')
       except OSError as error:
            print(error)

    
    with open(f'results/{fileName}-result.json', 'w', encoding='utf-8') as f: 
        json.dump(data, f, ensure_ascii=False, indent=2)

    