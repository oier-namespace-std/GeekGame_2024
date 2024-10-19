
MAXN = 2000
MAXM = 8000
MAXW = 10000

import random

M = (MAXN // 10 - 1) * (10) + (MAXN // 10) * (9) * 3 

print(f'{MAXN} {M} {1} {MAXN}')

# exit(0)

for i in range(MAXN // 10 - 1):
    for j in range(10):
        print(f'{i * 10 + j + 1} {i * 10 + j + 11} {random.randint(MAXW // 10, MAXW)}')
      #  print(f'{i * 10 + j + 1} {i * 10 + j + 11} {random.randint(MAXW // 10, MAXW)}')

for i in range(MAXN // 10):
    for j in range(9):
        print(f'{i * 10 + j + 1} {i * 10 + j + 2} {random.randint(10, 100)}')
        print(f'{i * 10 + j + 1} {i * 10 + j + 2} {random.randint(10, 100)}')
        print(f'{i * 10 + j + 1} {i * 10 + j + 2} {random.randint(10, 100)}')

