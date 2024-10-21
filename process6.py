# Sharing data between processes using multiprocessing.Lock
import multiprocessing
import time
def write1(lock):
    with open("file.txt",'w') as file:
        # lock.acquire()
        with lock:
            for _ in range(5):                   
                file.write("Kabul\n")
                time.sleep(1)
                print("write1")
        # lock.release()

def write2(lock):
    with open("file.txt",'w') as file:
        with lock:
            for _ in range(5):
                file.write("Berlin\n")
                time.sleep(1)
                print("write2")

lock=multiprocessing.Lock()
p1=multiprocessing.Process(target=write1,args=(lock,))
p2=multiprocessing.Process(target=write2,args=(lock,))

p1.start()
p2.start()
p1.join()
p2.join()