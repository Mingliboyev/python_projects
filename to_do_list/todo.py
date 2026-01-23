import os
import json

BASE=os.path.dirname(__file__)
PATH=os.path.join(BASE, "todo_list.json")

while True:
    command=int(input("""
        Show the whole list = 0
        Completed any task? = 1
        Adding a new task = 2
        Exit = 3
        
        What do you want to do: """))
    
    with open(PATH, 'r') as file:
        data=json.load(file)
    if command==0:
        for i in data:
            for k,v in i.items():
                print(f"{k} : {v}")
        t=int(input("\n\nMenu = 0: "))
        if t==0:
            continue        
    elif command==1:
        title=input("Which task have you completed: ")
        



    

