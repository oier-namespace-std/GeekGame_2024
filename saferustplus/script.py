import os

for i in range(32):
    os.system('python3 -u gen1.py | ./run >>log &')
