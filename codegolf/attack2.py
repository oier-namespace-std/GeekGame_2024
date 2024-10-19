from pwn import *

conn = process(argv = ['nc', 'prob19.geekgame.pku.edu.cn', '10019'])

print(conn.recvuntil(b'token: '), end = '>\n')
conn.sendline(b'165:MEQCIAO8Cvf2ewr9c8j2xJV-2MKt019qD2WRxsITgGZxEv-aAiApyfqPGe_LnG5HPuSqMFZzFLumbfL6yfGLiFS2WrnJQw==')

print(conn.recvuntil(b'Level: '), end = '>\n')
conn.sendline(b'3')

print(conn.recvuntil(b'expression: '), end = '>\n')
conn.sendline(b'(3**(n)+1)**(n-2+1//n)%(9**(n)-2)%(3**(n)-1)-1//n')

print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())

# flag{d0_u_usE_COmputaTI0N_by_r0Und1ng?}
# flag{mAG1c_geNerat1Ng_fUnct10N}
