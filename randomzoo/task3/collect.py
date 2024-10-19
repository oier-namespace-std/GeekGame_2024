import os
import time

for i in range(70, 256):
    print(f'getting log #{i}')
    os.system(f'python3 -u attack3.py >temp/{i}.log')
    time.sleep(16)

