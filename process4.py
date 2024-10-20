# Sharing data between processes using multiprocessing.Queue (first-in, first-out (FIFO) approach)
import multiprocessing

def myfunction(data):
    # New value is added to data variable
    data.put("Joya")
    
# Sharing data between two process
data=multiprocessing.Queue()

p1=multiprocessing.Process(target=myfunction,args=(data,))
p1.start()
p1.join()

print(data.get())