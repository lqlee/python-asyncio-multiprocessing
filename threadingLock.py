
import threading
import time

# Global variable to be accessed by multiple threads
shared_resource = 0

# Create a Lock object
resource_lock = threading.Lock()

def worker_function():
  """
  Function executed by each thread, modifying the shared resource.
  """
  global shared_resource
  for _ in range(1_000_000):
    # Acquire the lock before accessing the shared resource
    resource_lock.acquire()
    try:
      shared_resource += 1
    finally:
      # Release the lock after accessing the shared resource
      resource_lock.release()

if __name__ == "__main__":
    # Create multiple threads
    thread1 = threading.Thread(target=worker_function)
    thread2 = threading.Thread(target=worker_function)

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for both threads to complete
    thread1.join()
    thread2.join()

    print(f"Final value of shared_resource: {shared_resource}")
