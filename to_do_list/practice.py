import os,json

PATH=os.path.join(os.path.dirname(__file__), 'main.json')
with open(PATH, 'w') as file:
    json.dump([], file, indent=4)