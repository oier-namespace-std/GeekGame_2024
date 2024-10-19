from pwn import *

conn = process(argv = ['nc', 'prob02.geekgame.pku.edu.cn', '10002'])

print(conn.recvuntil(b'token:'), end = '>\n')
conn.sendline(b'165:MEQCIAO8Cvf2ewr9c8j2xJV-2MKt019qD2WRxsITgGZxEv-aAiApyfqPGe_LnG5HPuSqMFZzFLumbfL6yfGLiFS2WrnJQw==')

print(conn.recvuntil(b'"EOF")'), end = '>\n')
with open('attack2.html', 'r') as script:
    scr = script.read()
    conn.send(scr.encode('utf-8'))
    conn.sendline(b'')
    conn.sendline(b'EOF')

conn.interactive()
