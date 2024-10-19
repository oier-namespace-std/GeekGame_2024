from pwn import *

conn = process(argv = ['nc', 'prob07.geekgame.pku.edu.cn', '10007'])

print(conn.recvuntil(b'token:'), end = '>\n')
conn.sendline(b'165:MEQCIAO8Cvf2ewr9c8j2xJV-2MKt019qD2WRxsITgGZxEv-aAiApyfqPGe_LnG5HPuSqMFZzFLumbfL6yfGLiFS2WrnJQw==')

print(conn.recvuntil(b'[1/2]:'), end = '>\n')
conn.sendline(b'1')

conn.recvuntil(b'n = ')


N = int((conn.recvuntil(b'e = ').decode().split('\n'))[0])
e = int((conn.recvuntil(b'x0 = ').decode().split('\n'))[0])
x0 = int((conn.recvuntil(b'x1 = ').decode().split('\n'))[0])
x1 = int((conn.recvuntil(b'v = ').decode().split('\n'))[0])

print('e =', e)

# print(conn.recvuntil(b'buffer:'), end = '>\n')
mid = (x0 + x1) % N
if(mid % 2 == 1): mid += N
mid = mid >> 1
z = (mid + N - x0) % N

print('v =', mid + N)

conn.sendline(str(mid + N).encode('UTF-8'))

conn.recvuntil(b'v0 = ')
v0 = int((conn.recvuntil(b'v1 = ').decode().split('\n'))[0])
v1 = int((conn.recvuntil(b'\n').decode().split('\n'))[0])

print('v0 =', v0)
print('v1 =', v1)

D = (v0 + N - v1) % N
if(D % 2 == 1): D += N
D >>= 1

Z = pow(D, e, N)

det = (Z + N - z) % N

print('det =', det)

import math

# Now we have hacked this cryptosystem... 
# Its time to collect flags! 
q = math.gcd(det, N)
p = N // q

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

flag = (v0 + N * 3 - pow(p+q, d, N) - pow(mid + N - x0, d, N)) % N

print(flag.to_bytes(128, byteorder = 'big'))