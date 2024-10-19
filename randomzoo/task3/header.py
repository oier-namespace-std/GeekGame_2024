import os
import time

for i in range(128):
    with open(f'temp/{i}.log') as input:
        input.readline()
        input.readline()
        input.readline()
        fir = int(input.readline())
        print(fir, end = ', ')
