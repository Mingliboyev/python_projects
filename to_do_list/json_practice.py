import json
import os
PATH=os.path.dirname(__file__)
file_path=os.path.join(PATH, "todo_list.json")
with open(file_path, "r") as file:
    data=json.load(file)
title="Piano"
id="pi"
new_task={
    f"Task{len(data)+1}":{"title":title,"done":False, "id":id}
}
data.append(new_task)
with open(file_path, "w") as f:
    json.dump(data, f, indent=4)

