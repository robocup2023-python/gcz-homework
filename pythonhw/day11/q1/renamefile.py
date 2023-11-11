import os
import concurrent.futures
import time
import random
path = "files"
files = os.listdir(path)
def count_time(func):
    def wrapper():
        t1 = time.time()
        func()
        print('the run time is:',time.time()-t1)
    return wrapper
@count_time
def renameByOneThread():
    for file in files:
        name, extension = os.path.splitext(file)
        newname = f'{name}-new{extension}'
        src_path = os.path.join(path, file)
        dest_path = os.path.join(path, newname)
        os.rename(src_path,dest_path)
def task(files):
    for file in files:
        name, extension = os.path.splitext(file)
        newname = f'{name}-new{extension}'
        src_path = os.path.join(path, file)
        dest_path = os.path.join(path, newname)
        os.rename(src_path,dest_path)
@count_time
def renameByMultiThread():
    workers = 100
    chunksize = round(len(files) / workers)
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        for i in range(0, len(files), chunksize):
            filenames = files[i:(i + chunksize)]
            executor.submit(task, filenames)
if (__name__ == '__main__'):
    renameByOneThread()
    #renameByMultiThread()
