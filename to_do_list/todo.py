import os
import json
import time

def see_the_whole_list(data):
        if len(data)==0:
            print("Nothing in the list")
        else:    
            clear()
            for i in data:
                for k,v in i.items():
                    print(f"{v["title"]} : {'Done' if v['done']==True else 'Undone'}")
            time.sleep(3)
        input("\n\n\nType anything to back to Menu: ")
def mark_as_complete(data):        
    for i in data:
            for k,v in i.items():
                print(f"{v['id']} for {v['title']}")
        
    task_id=input("Write its ID: ").lower()
    for i in data:
        for k,v in i.items():
            if v["id"]==task_id:
                v["done"]=True
                print(f"{v['title']} marked as Completed!")
                with open(PATH, "w") as f:
                    json.dump(data, f, indent=4)

                break
        break
    input("\n\n\nType anything to back to Menu: ")
def add_new_task(data):
    task=input("Enter the name of a new task: ").capitalize()
    time.sleep(2)
    task_id=input(f"Please enter 2 or 3-letter word as an ID for {task}: ")
    new_task = {
        f"task{len(data)+1}":{
            "title":task, "done":False, "id":task_id
        }
    }
    data.append(new_task)
    print(f"Added a new task: {task}")
    with open(PATH, "w") as file:
        json.dump(data, file, indent=4)

    print("Saved all changes")
    time.sleep(2)
    input("\n\n\nType anything to back to Menu: ")

    
PATH=os.path.join(os.path.dirname(__file__), "todo_list.json")

def clear():
    os.system("cls" if os.name == "nt" else "clear")
def todo_list():
    while True:
        command=int(input("""
            Show the whole list = 0
            Completed any task? = 1
            Adding a new task = 2
            Exit = 3
        
            What do you want to do: """))
        try:
            with open(PATH, "r") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            data = []

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


        





    

