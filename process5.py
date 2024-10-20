import multiprocessing

def fun1(data,q):
    
    q.put(data)

def fun2(data,q):
    q.put(str(data)+"A")

var=20
q=multiprocessing.Queue()
p1=multiprocessing.Process(target=fun1,args=(var,q))
p2=multiprocessing.Process(target=fun2,args=(var,q))

p1.start()
p2.start()
p1.join()
p2.join

while q.empty() is False:
    print(q.get())