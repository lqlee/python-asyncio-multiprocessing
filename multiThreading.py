
import asyncio
import time
import threading

def mysleep(n) :
  print(f'enter sleep, tid : {threading.get_ident()}')
  time.sleep(n)


async def play (init_event) :
  await init_event.wait()
  print(f'enter play, tid : {threading.get_ident()}')
  for _ in range(5) : # 5 times/rounds
#await asyncio.sleep(1) # sleep 1 second
#await asyncio.to_thread(time.sleep, 1)
    await asyncio.to_thread(mysleep, 1)
    for _ in range(1000) :
      pass
  print('exit play')

async def main() :
  print('enter main')
  start = time.time()
  init_event = asyncio.Event()
  tasks = [play(init_event) for _ in range(10)]
  print('Init start ...')
  await asyncio.sleep(1)
  print('Init done ...')
  init_event.set()
  await asyncio.gather(*tasks)
  print(f'total time : {time.time() - start} seconds')

# main()
asyncio.run(main())

'''
Lock
lock = asyncio.Lock()
await lock.aquire()
try :
  ...
finally :
  lock.release()

lock = asyncio.Lock()
async with lock:

Barrier
barrier = asyncio.Barrier(2)
await barrier.wait()

barrier = asyncio.Barrier(2)
async with barrier:

Semaphore
sem = asyncio.Semaphore(10)
await sem.acquire()
try :
  ...
finally :
  sem.release()

sem = asyncio.Semaphore(10)
async with sem:
  ...

Condition
cond = asyncio.Condition()
await cond.acquire()
try :
  await cond.wait()
finally :
  cond.release()

cond = asyncio.Condition()
await cond.wait()


'''
