import copy
buf = ''
read = False
frame_size = 0
cur_size = 0
frames = []
try:
    ibuf = []
    while(True):
        buf = input()
        if(buf[0:8] == '// Frame'):
            assert(frame_size == cur_size)
            if(len(ibuf) != 0):
                key = ibuf[3] + ibuf[4] * 256 + ibuf[5] * 256 ** 2 + ibuf[6] * 256 ** 3
                frames.append((key, copy.deepcopy(ibuf)))
                ibuf = []
            read = False
        if(buf[0:21] == '// Unescaped RSP Data'):
            read = True
            frame_size = int(buf[23:27])
            cur_size = 0
        
        sp = buf.split(',')
        for s in sp:
            t = s.strip()
            if(t[-4:-2] == '0x'):
                d = int(t[-2:], 16)
                if(read):
                    ibuf.append(d)
                    cur_size = cur_size + 1
except EOFError:
    if(len(ibuf) != 0):
        key = ibuf[3] + ibuf[4] * 256 + ibuf[5] * 256 ** 2 + ibuf[6] * 256 ** 3
        frames.append((key, copy.deepcopy(ibuf)))
    pass

# frames.sort()
print('total frames:', len(frames))

out = open('dmp.264', 'wb')

counter = 0
for d in frames[0][1]:
    out.write(d.to_bytes(1, 'little'))
for f in frames[1400:]:
    counter = counter + 1
    # print(f[1])
    for d in f[1]:
        out.write(d.to_bytes(1, 'little'))

# flag{BigBrotherIsWatchingYou!!} 
 