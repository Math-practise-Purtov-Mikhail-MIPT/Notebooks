from functools import lru_cache

@lru_cache(maxsize=None)
def f(m , n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return f(m - 1, 1)
    elif m > 0 and n > 0:
        return f(m - 1, f(m, n - 1))
    
import sys
sys.setrecursionlimit(10**6)

for i in range(5):
    for j in range(5):
        print(f(i, j), end=' ')
    print()
