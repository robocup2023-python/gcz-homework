import time
import pandas as pd
import os
import multiprocessing
import re
import threading
import concurrent.futures
def task(para):
    lst = para[0]
    n = para[1]
    dic = {}
    for i in range(len(lst)):
        dic[i] = lst[i]*n
    return dic
if __name__ == "__main__":
    processes = []
    with concurrent.futures.ThreadPoolExecutor() as pe:
        res = pe.map(task, [([1,2,3],2),([4,5,6],3),([55],4)])
    for i in res:
        print(i)
    dic = {"i":2, "love":3, "you":4}
    dics = {}
    dic2 = {"i":4, "then":4}
    dics.update(dic)
    dics.update(dic2)
    print(dics)