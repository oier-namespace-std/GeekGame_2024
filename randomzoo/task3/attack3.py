from pwn import *

conn = process(argv = ['nc', 'prob17.geekgame.pku.edu.cn', '10017'])

print(conn.recvuntil(b'token: '), end = '>\n')
conn.sendline(b'165:MEQCIAO8Cvf2ewr9c8j2xJV-2MKt019qD2WRxsITgGZxEv-aAiApyfqPGe_LnG5HPuSqMFZzFLumbfL6yfGLiFS2WrnJQw==')

for _ in range(128):
    z = str(conn.recvuntil(b'\n'))
    x = int(z[2:-3])
    print(x)
    conn.sendline(b'\n')
