from multiprocessing import Process, Lock, Value

def increment_counter(counter, lock):
    for _ in range(1000):
        with lock:
            counter.value += 1

if __name__ == "__main__":
    # Shared counter between processes
    counter = Value('i', 0)  # 'i' is for integers
    lock = Lock()

    # Create multiple processes
    processes = [Process(target=increment_counter, args=(counter, lock)) for _ in range(5)]

    # Start the processes
    for p in processes:
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()

    # Output the final counter value
    print(f"Final counter value: {counter.value}")
