from multiprocessing import Process, Array

def increment_array(shared_array):
    for i in range(len(shared_array)):
        shared_array[i] += 1  # Increment each element of the array

def decrement_array(shared_array):
    for i in range(len(shared_array)):
        shared_array[i] -= 1  # Decrement each element of the array

if __name__ == "__main__":
    # Create a shared array of integers with initial values [0, 1, 2, 3, 4]
    shared_array = Array('i', [0, 1, 2, 3, 4])  # 'i' indicates integers

    print("Initial array:", shared_array[:])

    # Create two processes: one to increment, one to decrement the array
    p1 = Process(target=increment_array, args=(shared_array,))
    p2 = Process(target=decrement_array, args=(shared_array,))

    p1.start()
    p2.start()

    # Wait for both processes to finish
    p1.join()
    p2.join()

    # After both processes, the array should be the same as the initial value
    print("Final array:", shared_array[:])
