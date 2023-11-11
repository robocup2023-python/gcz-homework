import threading
from threading import Lock,Thread
import time,os
g_num = {}
def work():
    global  g_num
    count = g_num.get("name")
    if count != None:
        count += 1
        g_num["name"] = count
    else:
        g_num["name"] = 1
    print(g_num["name"])

if __name__ == '__main__':
    t1 = threading.Thread(target=work)
    t2 = threading.Thread(target=work)
    t1.start()
    t2.start()