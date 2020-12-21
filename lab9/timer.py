import time

def timer(x):
    if x == 0:
        print("the end")
        return None
    print(x)
    time.sleep(1)
    timer(x-1)
    
timer(5)