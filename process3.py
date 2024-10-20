# Sharing data between two processes using multiprocessing.Value
import multiprocessing

def add(data):
    # New value is added to data variable
    data.value=data.value+55
    
# Sharing data between two process
data=multiprocessing.Value("d",88.77) # 'i' indicates integers, also 'd' indicates doubles

p1=multiprocessing.Process(target=add,args=(data,))
p1.start()
p1.join()

print(data.value)

      
