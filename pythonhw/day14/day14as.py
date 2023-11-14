import time
import pandas as pd
import os
import multiprocessing
import re
import threading
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
path = "download/Texts"
files = os.listdir(path)
pattern = r'<w[^>]*>(\w+)\s*</w>'
lock = threading.Lock()
dic = {}
def count_time(func):
    def wrapper():
        t1 = time.time()
        func()
        print('the run time is:',time.time()-t1)
    return wrapper
import time


def count_time_with_return(func):
    def wrapper():
        t1 = time.time()
        res = func()
        t2 = time.time()

        # 计算时间
        time_consumed = t2 - t1
        print('{}函数一共花费了{}秒'.format(func.__name__, time_consumed))
        return res
    return wrapper

@count_time
def count_words_with_one_thread():
    for file in files:
        with open(os.path.join(path, file), 'r') as f:
            content = f.read()
        words = re.findall(pattern, content)
        for word in words:
            if dic.get(word)!=None:
                dic[word] = dic[word] + 1
            else:
                dic[word] = 1
def task(filenames):
    dic = {}
    for file in filenames:
        with open(os.path.join(path, file), 'r') as f:
            content = f.read()
        words = re.findall(pattern, content)
        for word in words:
            if dic.get(word)!=None:
                dic[word] = dic[word] + 1
            else:
                dic[word] = 1
    return dic
def multithread(filenames):
    numberofthread = 4
    chunk_size = round(len(filenames)/numberofthread)
    split_files = [filenames[i:i+chunk_size] for i in range(0,len(filenames),chunk_size)]
    with ThreadPoolExecutor(max_workers=4) as pool:
        res = pool.map(task, split_files)
    dics = {}
    for dic in res:
        dics.update(dic)
    return dics      
@count_time_with_return
def count_words_with_multithread():
    numberofprocess = 2
    chunk_size = round(len(files)/numberofprocess)
    #processes = []
    paras = [files[i:i + chunk_size] for i in range(0,len(files),chunk_size)]
    with ProcessPoolExecutor(max_workers=2) as pool:
        res = pool.map(multithread, paras)
    # for i in range(0,len(files),chunk_size):
    #     processes.append(multiprocessing.Process(target=multithread,args=(files[i:i + chunk_size],queue)))
    # for process in processes:
    #     process.start()
    # for process in processes:
    #     process.join()
    dics = {}
    for dic in res:
        dics.update(dic)
    return dics

if __name__ == "__main__":
    dics = count_words_with_multithread()
    #count_words_with_one_thread()
    df = pd.DataFrame(list(dics.items()), columns=["word","time"])
    df.to_csv('words.csv',encoding='utf-8')