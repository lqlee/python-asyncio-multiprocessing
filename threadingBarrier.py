
import threading
import time
import random

def worker_task(thread_id, barrier):
  """
  A function representing the work done by each thread,
  including waiting at a barrier.
  """
  print(f"Thread {thread_id}: Starting work...")
  time.sleep(random.uniform(0.5, 2.0))  # Simulate some work

  print(f"Thread {thread_id}: Reached the barrier. Waiting for others...")
  try:
    # Wait at the barrier. The wait() method returns an integer
    # representing the "phase" of the barrier, or raises BrokenBarrierError
    # if the barrier is broken or times out.
    barrier.wait()
    print(f"Thread {thread_id}: Barrier lifted. Proceeding...")
  except threading.BrokenBarrierError:
    print(f"Thread {thread_id}: Barrier was broken. Exiting.")

if __name__ == "__main__":
  num_threads = 4
  # Create a barrier for 'num_threads' parties.
  # An optional 'action' callable can be provided, which is executed by
  # one of the threads when the barrier is lifted.
  barrier = threading.Barrier(num_threads)

  threads = []
  for i in range(num_threads):
    thread = threading.Thread(target=worker_task, args=(i, barrier))
    threads.append(thread)
    thread.start()

  # Wait for all worker threads to complete
  for thread in threads:
    thread.join()

  print("All threads have completed their tasks.")
