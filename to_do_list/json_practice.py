import json
import os
PATH=os.path.dirname(__file__)
file=os.path.join(PATH, "todo_list.json")
with open(file, "r") as file:
    data=json.load(file)
print(data)
