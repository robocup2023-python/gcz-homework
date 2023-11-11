import time
import pandas as pd
import os
import multiprocessing
import re
import threading
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
    global dic
    for file in filenames:
        with open(os.path.join(path, file), 'r') as f:
            content = f.read()
        words = re.findall(pattern, content)
        for word in words:
            lock.acquire()
            if dic.get(word)!=None:
                dic[word] = dic[word] + 1
            else:
                dic[word] = 1
            lock.release()
@count_time
def multithread():
    numberofthread = 4
    chunk_size = round(len(files)/numberofthread)
    threads = []
    for i in range(0,len(files),chunk_size):
        threads.append(threading.Thread(target=task, args=(files[i:i+chunk_size],)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
@count_time
def count_words_with_multithread():
    numberofprocess = 2
    chunk_size = round(len(files)/numberofprocess)
    processes = []
    for i in range(0,len(files),chunk_size):
        processes.append(multiprocessing.Process(target=multithread,args=(files[i:i + chunk_size],)))
    for process in processes:
        process.start()
    for process in processes:
        process.join()

if __name__ == "__main__":
    #multithread()
    #count_words_with_multithread()
    count_words_with_one_thread()
    df = pd.DataFrame(list(dic.items()), columns=["word","time"])
    df.to_csv('words.csv',encoding='utf-8')