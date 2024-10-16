
import time
import threading

data=[]
def calc_square(numbers):
    for n in numbers:
        time.sleep(0.2)
        print("Square: ",n*n)
        data.append(n)
    print("This result is inside process: ", data)


def calc_cube(numbers):
    for n in numbers:
        time.sleep(0.2)
        print("Cube: ",n*n*n)


arr=[2,3,4,5]

t=time.time()

# calc_square(arr)
# calc_cube(arr)
t1=threading.Thread(target=calc_square,args=(arr,))
t2=threading.Thread(target=calc_cube,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()
print("This result is outside process: ",data)
print("Time: ",time.time()-t)

