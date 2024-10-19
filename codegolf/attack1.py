from pwn import *

conn = process(argv = ['nc', 'prob19.geekgame.pku.edu.cn', '10019'])

print(conn.recvuntil(b'token: '), end = '>\n')
conn.sendline(b'165:MEQCIAO8Cvf2ewr9c8j2xJV-2MKt019qD2WRxsITgGZxEv-aAiApyfqPGe_LnG5HPuSqMFZzFLumbfL6yfGLiFS2WrnJQw==')

print(conn.recvuntil(b'Level: '), end = '>\n')
conn.sendline(b'1')

print(conn.recvuntil(b'expression: '), end = '>\n')
conn.sendline(b'665772//2**n%2+(9**9+n%19-n**92160%510510)//9**9')

print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())

# flag{N0t_FU11y_Re1iAble_pRiMe_t3st}
