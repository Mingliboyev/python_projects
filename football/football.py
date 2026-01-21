import random
import time
CLEAR="\033[2J"
def you_as_kicker(reps=3):
    keep=0
    you=0
    for _ in range(reps):
        print(CLEAR)
        direction=input("Where to kick (left, middle, right): ")
        print("Shouts...")
        time.sleep(2)
        keeper=random.choice(["left","middle","right"])
        print(f"Keeper jumped to {keeper}")
        if direction==keeper:
            keep+=1
        else:
            you+=1
        time.sleep(2)   
        print(f"| Keeper | {keep} : {you} | You |")
        time.sleep(2)
    return you 

def you_as_keeper(reps=3):
    you=0
    kicker_score=0
    for _ in range(reps):
        print(CLEAR)
        kicker=random.choice(["left", "middle", "right"])
        user=input("Where do you jump (left, middle, right): ")
        print("Booom...")
        time.sleep(2)
        print(f"Kicker shot to the {kicker}")
        if kicker==user:
            you+=1
        else:
            kicker_score+=1
        time.sleep(2)
        print(f"| Kicker | {kicker_score} : {you} | You |")
        time.sleep(2)
    return kicker_score

def game(reps):
    print(CLEAR)
    print("""Hello, Ladies and gentlemen!""")
    time.sleep(5)
    print("Now it is Jahongir`s turn to shot the ball. Lets watch!")
    time.sleep(5)
    print(CLEAR)

    a=you_as_kicker(reps)
    time.sleep(5)
    print("OK, Not that bad! Now computer will kick it! No words here. Just watch!")
    time.sleep(5)
    print(CLEAR)
    b=you_as_keeper(reps)
    time.sleep(5)
    print(CLEAR)
    print(f"Overall score: \n | Kicker | {b} : {a} | You |\n\n\n")
    time.sleep(5)
    print(CLEAR)
    if a>b:
        print("Congratulations! You win\n\n\n")
    elif a<b:
        print("You loose!\n\n\n")
    else:
        print("Congratulation with draw!\n\n\n")
game(3)