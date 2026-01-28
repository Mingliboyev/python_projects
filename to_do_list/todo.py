import os
import json
import time

PATH=os.path.join(os.path.dirname(__file__), "todo_list.json")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def see_the_whole_list(data):
        if len(data)==0:
            print("Nothing in the list")
        else:    
            clear()
            for i in data:
                print(f"{i['title']} : {'Done' if i['done']==True else 'Undone'}")
            time.sleep(3)
def mark_as_complete(data):        
    all_ids=[]
    for i in data:
        print(f"{i['id']} for {i['title']}")
        all_ids.append(i['id'])    
    while True:
        task_id=int(input("Write its ID: "))
        if task_id in all_ids:
            break
        else:
            print(f"{task_id} doesn`t exist")
        
    for i in data:
        if i["id"]==task_id:
            i["done"]=True
            print(f"{i['title']} marked as Completed!")
            with open(PATH, "w") as f:
                json.dump(data, f, indent=4)
            break
    time.sleep(3) 
def add_new_task(data):
    task=input("Enter the name of a new task: ").capitalize()
    new_task = {
        "title":task,"id":len(data)+1,"done":False
    }
    data.append(new_task)
    print(f"Added a new task: {task}")
    with open(PATH, "w") as file:
        json.dump(data, file, indent=4)

    print("Saved all changes")
    time.sleep(2)

    
def todo_list():
    while True:
        try:
            with open(PATH, "r") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            data = []
        
        command=int(input("""
            Show the whole list = 0
            Completed any task? = 1
            Adding a new task = 2
            Exit = 3
        

            What do you want to do: """))
        if command==0:
            see_the_whole_list(data)
        elif command==1:
            mark_as_complete(data)
        elif command==2:
            add_new_task(data)
        elif command==3:
            print("Thanks for using...")
            time.sleep(2)
            break        

todo_list()
