from numba.np.ufunc import parallel
import numpy as np
import numba

def fibonacirecursivo(x:int):
  return  x if x < 2 else fibonacirecursivo(x - 1) + fibonacirecursivo(x - 2) 

@numba.jit(parallel=True, nopython=True)
def fibonacirecursivootimizado(x:int):
  return  x if x < 2 else fibonacirecursivo(x - 1) + fibonacirecursivo(x - 2) 

def fibonacidinamico(x:int):
  datatable = np.arange(0, x)

  if x <= 1:
    return datatable[1]

  for index in range(2, x):
    datatable[index] = datatable[index - 1] + datatable[index - 2]
  
  return datatable[x - 1]

@numba.jit(parallel=True, nopython=True)
def fibonacidinamicootimizado(x:int):
  datatable = np.arange(0, x)

  if x <= 1:
    return datatable[1]

  for index in range(2, x):
    datatable[index] = datatable[index - 1] + datatable[index - 2]

  return datatable[x - 1]

