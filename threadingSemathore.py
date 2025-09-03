
import threading
import time
import random

# Create a Semaphore with a maximum of 3 concurrent accesses
semaphore = threading.Semaphore(3)

def worker(thread_id):
  print(f"Thread {thread_id}: Attempting to acquire semaphore...")
  with semaphore:  # Acquire the semaphore
    print(f"Thread {thread_id}: Acquired semaphore. Working...")
    # Simulate some work
    sleep_time = random.uniform(1, 3)
    time.sleep(sleep_time)
    print(f"Thread {thread_id}: Finished work. Releasing semaphore...")
    # Semaphore is automatically released when exiting the 'with' block

if __name__ == "__main__":
  threads = []
  for i in range(10):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

  # Wait for all threads to complete
  for thread in threads:
    thread.join()

  print("All threads finished.")
