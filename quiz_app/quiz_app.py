import json
import os
import random
PATH=os.path.join(os.path.dirname(__file__), "quiz_questions.json")
with open(PATH, "r") as file:
    data=json.load(file)
counter=0
asked=0
while asked<len(data):
    q=random.choice(data)
    while q['Asked']!=False:
        q=random.choice(data)
    q["Asked"]=True
    asked+=1    
    print(q['question'])
    for i,y in q['options'].items():
        print(f"{i}){y}")
    answer=input("\n\n\nYour Answer: ")
    if answer==q['answer']:
        print("True")
        counter+=1
    else:
        print("False")
    print(f'You have {counter} correct answers so far.')
    con=input("Do you want to continue? (y/n): ").lower()=="y"
    if not con:
        break
    
