"""
The multiprocessing.Pool in Python provides a convenient way to parallelize the execution of 
a function across multiple input values. 
It manages a pool of worker processes, distributing tasks (work) to each process, 
and collects the results once they are complete. 
This helps in performing tasks concurrently using multiple CPU cores, 
improving performance for compute-bound or parallelizable workloads.
"""

from multiprocessing import Pool
import time

def myfunc(n):
    time.sleep(1)
    return n*n

numbers=[2,3,4,5,6,7,8]

# with Pool(4) as p:

p=Pool(processes=4)
result=p.map(myfunc,numbers)
p.close()
p.join()
print(result)