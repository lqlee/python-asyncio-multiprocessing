
import asyncio
import time

async def play () :
  print('enter play')
  for _ in range(2) :
    await asyncio.sleep(1)
    for _ in range(1000) :
      pass

async def main() :
  print('enter main')
  start = time.time()
  '''
  tasks = []
  for _ in range(10) :
    tasks.append(play())'''
  await asyncio.gather(*[play() for _ in range(10)])
  print(f'total time : {time.time() - start} seconds')

# main()
asyncio.run(main())
