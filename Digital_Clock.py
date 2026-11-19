import time

while True:
    now = time.strftime("%H:%M%S")
    print("\rTIME :", now, end="")
    time.sleep(1)
    
