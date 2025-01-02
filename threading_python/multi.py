import multiprocessing
import time
from threading import Thread


def cpu_bound_task(n):
    return sum(i * i for i in range(n))


if __name__ == "__main__":
    n = 10**7  # Large number for the CPU-bound task

    # Using multiprocessing
    start_time = time.time()
    processes = []
    for _ in range(4):  # Create 4 processes
        p = multiprocessing.Process(target=cpu_bound_task, args=(n,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()  # Wait for all processes to finish

    print(f"Multiprocessing took {time.time() - start_time:.2f} seconds.")

    # without multi processing

    start_time = time.time()
    cpu_bound_task(10**7)

    print(f"Single processing took {time.time() - start_time:.2f} seconds.")

    # using threading

    start_time = time.time()

    threads = []
    for _ in range(4):  # Create 4 threads
        t = Thread(target=cpu_bound_task, args=(n,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()  # Wait for all threads to finish

    print(f"Threading took {time.time() - start_time:.2f} seconds.")
