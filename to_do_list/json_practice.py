data=[{'title':'welo', 'id':1}]
all_ids=[]
for i in data:
    print(f"{i['id']} for {i['title']}")
    all_ids.append(i['id'])    
while True:
    task_id=input("Write its ID: ")
    if task_id in all_ids:
        break
    else:
        print(f"{task_id} doesn`t exist")