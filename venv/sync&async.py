import threading
import time


def a():
    print("function a is starting")
    time.sleep(1)
    for i in range(5):
        print(i)
        time.sleep(1)
    print("function a is ending")
    time.sleep(1)


def b():
    print("function b is starting")
    time.sleep(1)
    for i in range(7):
        print(i)
        time.sleep(1)
    print("function b is ending")
    time.sleep(1)


t1 = threading.Thread(target=a)
t2 = threading.Thread(target=b)

# sync
t1.start()
t1.join()
t2.start()
t2.join()

# async
t1.start()
t2.start()
t1.join()
t2.join()
