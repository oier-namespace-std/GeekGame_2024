from pwn import *

conn = process(argv = ['nc', 'prob07.geekgame.pku.edu.cn', '10007'])

print(conn.recvuntil(b'token:'), end = '>\n')
conn.sendline(b'165:MEQCIAO8Cvf2ewr9c8j2xJV-2MKt019qD2WRxsITgGZxEv-aAiApyfqPGe_LnG5HPuSqMFZzFLumbfL6yfGLiFS2WrnJQw==')

print(conn.recvuntil(b'[1/2]:'), end = '>\n')
conn.sendline(b'2')

conn.recvuntil(b'n = ')


N = int((conn.recvuntil(b'e = ').decode().split('\n'))[0])
e = int((conn.recvuntil(b'x0 = ').decode().split('\n'))[0])
x0 = int((conn.recvuntil(b'x1 = ').decode().split('\n'))[0])
x1 = int((conn.recvuntil(b'v = ').decode().split('\n'))[0])

print('e =', e)

# print(conn.recvuntil(b'buffer:'), end = '>\n')
mid = (x0 + x1) % N
if(mid % 2 == 1): mid += N
mid = mid >> 1
z = (mid + N - x0) % N

print('v =', mid + N)

conn.sendline(str(mid + N).encode('UTF-8'))

conn.recvuntil(b'v0 = ')
v0 = int((conn.recvuntil(b'v1 = ').decode().split('\n'))[0])
v1 = int((conn.recvuntil(b'\n').decode().split('\n'))[0])

print('v0 =', v0)
print('v1 =', v1)

R = (v0 + v1) % N

print('N =', N)
print('R =', R)

# exit(0)
# fxxking coppersmith 

flag = 71924130236548371627431107207903806177673986003338811201957954020478533872482528066170780149702175181181400388122947673706020907241391707677352351053439919979819012280327957341027296591153723448709015281846725814913113541766019644730153306878732483881918213332486175853032846943438459563067009609829306293236

print(flag.to_bytes(128, byteorder = 'big'))

# flag{WhAt-If-h1DDEn-mOduLUS-M33ts-C0ppersMIth?!}

exit(0)
