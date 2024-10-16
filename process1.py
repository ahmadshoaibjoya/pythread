import multiprocessing
import time
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

p1=multiprocessing.Process(target=calc_square,args=(arr,))
p2=multiprocessing.Process(target=calc_cube,args=(arr,))

p1.start()
p2.start()

p1.join()
p2.join()
# calc_square(arr)
# calc_cube(arr)
print("This result is outside process: ",data)
print("Time: ",time.time()-t)