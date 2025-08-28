
import pi
import time
import multiprocessing as mp

iter_round = 100_000_000

def single_process() -> float :
  return pi.calculate_pi(0, iter_round)

def calculate_pi_wrapper(res, start, end) :
  res.value = pi.calculate_pi(start, end)


def multi_process() :
  step = iter_round // 10
  procs = []
  for start in range(0, iter_round, step) :
    res = mp.Value('d')
    p = mp.Process(target=calculate_pi_wrapper, args=[res, start, start + step])
    p.start()
    procs.append((p, res))

    pi = 0.0
  for p, v in procs :
    p.join()
    pi += v.value

  return pi

def multi_process_pool () :
  params = []
  step = iter_round // 10
  for start in range(0, iter_round, step) :
    params.append((start, start + step))

  with mp.Pool(10) as pool :
    res = pool.starmap(pi.calculate_pi, params)

  return sum(res)  



def main() -> None :
  start_time = time.time()
  print(single_process())
  print(f'single_process: {time.time() - start_time} seconds')

  start_time = time.time()
  print(multi_process())
  print(f'multi_process: {time.time() - start_time} seconds')

  start_time = time.time()
  print(multi_process_pool())
  print(f'multi_process_pool: {time.time() - start_time} seconds')


if __name__ == '__main__' :
  main()
