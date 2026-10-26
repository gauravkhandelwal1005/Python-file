import threading 
import time

def print_numbers():
    for i in range(1, 4):
        time.sleep(0.5)
    print(f"Thread 1: {i}")
    
def print_letter():
    for letter in ['A', 'B', 'C']:
        time.sleep(0.5)
        print(f"Thread 2: {letter}")
    
t1 = threading.Thread(target = print_numbers)
t2 = threading.Thread(target = print_letter)

t1.start()
t2.start()

t1.join()
t2.join()
