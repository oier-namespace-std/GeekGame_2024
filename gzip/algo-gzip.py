# FROM debian:12
# RUN apt update && apt install -y python3 python3-pip

import random
import gzip

from pathlib import Path
try:
    FLAG1 = Path('/flag1').read_text().strip()
    FLAG2 = Path('/flag2').read_text().strip()
except Exception:
    FLAG1 = 'fake{get flag1 on the real server}'
    FLAG2 = 'fake{get flag2 on the real server}'

def average_bit_count(s):
    # print(s)
    ret = 0
    for c in s:
        # print(c)
        r = int(c)
        while(r > 0):
            # print(r)
            ret += r & 1
            r = r // 2
    # print(ret)
    
    return ret / len(s)
    # return sum(c.bit_count() for c in s) / len(s)

def main():
    text = input('Input text: ')
    IN = text
    assert len(text)<=1000
    assert all(0x20<=ord(c)<=0x7e for c in text)
        
    # text = [ord(c) for c in text]
    text = [ord(c) ^ 22 for c in text]

    print('After xor:')
    print(text)

    random.seed('YuanShen')
    random.shuffle(text)

    print('After shuffle:')
    print(text)
    # text = b'\x1f\x8b\x08\x00\xebh\ng\x11\xff3\x03\x00\x14z\xb8\x1d\x01\x00\x00\x00\x00'
    # text = gzip.decompress(bytes(text))

    #print('Temp text:')
    #print(text)
    text = gzip.compress(bytes(text))
    print('After processing:')
    print(text)
    
    prefix = (text + b'\xFF'*256)[:256]

    print(prefix)

    print('abc: ', average_bit_count(prefix))
    
    if average_bit_count(prefix) < 2.5:
        with open('inp1', 'w') as o1:
            o1.write(IN)
        print('\nGood! Flag 1: ', FLAG1)
    
    if b'[What can I say? Mamba out! --KobeBryant]' in text:
        with open('inp2', 'w') as o2:
            o2.write(IN)
        print('\nGood! Flag 2: ', FLAG2)

main()