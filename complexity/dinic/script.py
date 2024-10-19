MAXN = 100
MAXM = 5000
MAXW = 10000

import random



# exit(0)

N1 = MAXN // 3
N2 = MAXN // 3
M = N1 * N2 + N1 + N2 + (MAXN - N1 - N2 - 3) + 1

print(f'{MAXN} {MAXM} {1} {2}')

for i in range(N1):
    for ii in range(N2):
        print(f'{i + 3} {ii + N1 + 3} {1}')

for i in range(N1):
    print(f'{1} {i + 3} {100}')

for i in range(N2):
    print(f'{i + N1 + 3} {N1 + N2 + 3} {100}')

for i in range(MAXN - N1 - N2 - 3):
    print(f'{i + N1 + N2 + 3} {i + N1 + N2 + 4} {10000}')


print(f'{MAXN} {2} {10000}')

for i in range(MAXM - M):
    print(f'{MAXN} {MAXN - 1} {1}')