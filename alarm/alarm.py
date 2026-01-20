import time
import winsound
CLEAR="\033[2J"
CLEAR_AND_RETURN="\033[H"
def alarm(seconds):
    print(CLEAR)
    i=1
    while i<=seconds:
        time.sleep(1)
        left_minutes=(seconds-i)//60
        left_seconds=(seconds-i)%60
        print(CLEAR_AND_RETURN)
        print(f"Remaining: {left_minutes:02d}:{left_seconds:02d}")
        i+=1
    winsound.PlaySound("d:\\programming\\python\\alarm.wav", winsound.SND_FILENAME)

minutes=int(input("How many minutes: "))
seconds=int(input("How many seconds: "))
total=minutes*60+seconds
alarm(total)
        
