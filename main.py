# Problema de cacching offline

def next():
  return 

def p_caching_offline(k:int, v:list[int]) ->:
  cache:dict[list[int]] = {}
  
  for i, k in enumerate(v):
    if k in cache.keys():
      cache[i].append(k)
    else:
      cache[i] = [i]
  
  while i < k and i < len(v):
    cache[i] = v[i]
    miss += 1
  
  while i < len(v):
    next(cache, v[i], i)  

if __name__ in '__main__':
  v:int  =[4,1,2,3,4,4,1,4,4,2,4]
  k:int = 4