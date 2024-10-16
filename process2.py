# Sharing data between two processes using multiprocessing.Array

import multiprocessing

def calc_square(numbers,data):
    
    # for index, n in enumerate(numbers):
    #     data[index]=n*n
    #     print("Square: ",n*n)

    i=0
    for n in numbers:
        data[i]=n*n
        print("Square: ",n*n)
        i+=1    


arr=[2,3,4,5]
# Sharing data between two process
data=multiprocessing.Array("i",4) # 'i' indicates integers, also 'd' indicates doubles

p1=multiprocessing.Process(target=calc_square,args=(arr,data))
p1.start()
p1.join()

print(data[:])
      
