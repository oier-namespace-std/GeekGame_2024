from pwn import *
import random

# https://book.jorianwoltjer.com/cryptography/pseudo-random-number-generators-prng
import library
from library import Untwister

# library.test()

conn = process(argv = ['nc', 'prob16.geekgame.pku.edu.cn', '10016'])

print(conn.recvuntil(b'token: '), end = '>\n')
conn.sendline(b'165:MEQCIAO8Cvf2ewr9c8j2xJV-2MKt019qD2WRxsITgGZxEv-aAiApyfqPGe_LnG5HPuSqMFZzFLumbfL6yfGLiFS2WrnJQw==')

ut = Untwister()

lThreshold = 16
rThreshold = 32 - lThreshold

for _ in range(1300):
    z = str(conn.recvuntil(b'\n'))
    # print(z)
    x = int(z[2:-3])
    conn.sendline(b'')
    higher = (x >> lThreshold) | (1 << rThreshold)
    # print(bin(higher)[3:])
    ut.submit(bin(higher)[3:] + "?"*lThreshold)
# this has chance to fail since the lower (17-th) bits may be corrupted by adding a char 
# flag{mT19937_cAN_BE_AtTACKeD} 

predictor = ut.get_random()

for _ in range(200):
    z = str(conn.recvuntil(b'\n'))
    # print(z)
    x = int(z[2:-3])
    conn.sendline(b'')
    randNext = predictor.getrandbits(32)
    # print(x, randNext)
    print(chr(x - randNext), end = '')
