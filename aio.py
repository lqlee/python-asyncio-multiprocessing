
import asyncio
import time

async def play () :
  print('enter play')
  for _ in range(5) : # 5 times/rounds
    await asyncio.sleep(1) # sleep 1 second
    for _ in range(1000) :
      pass

async def main() :
  print('enter main')
  start = time.time()
  await asyncio.gather(*[play() for _ in range(10)])
  print(f'total time : {time.time() - start} seconds')

# main()
asyncio.run(main())
