import time
import pandas as pd
import os
import multiprocessing
import re
import threading
def task():
    n = 0
    n+=1
    print(n)
if __name__ == "__main__":
    processes = []
    for i in range(2):
        processes.append(multiprocessing.Process(target=task))
    for process in processes:
        process.start()
    for process in processes:
        process.join()