import copy
buf = ''
read = True
frame_size = 0
cur_size = 0
frames = []
try:
    ibuf = []
    while(True):
        buf = input()
        if(buf[0:8] == '// Frame'):
            if(len(ibuf) != 0):
                key = ibuf[0x2b]
                frames.append((key, copy.deepcopy(ibuf)))
                ibuf = []
        
        sp = buf.split(',')
        for s in sp:
            t = s.strip()
            if(t[-4:-2] == '0x'):
                # print(t)
                d = int(t[-2:], 16)
                if(read):
                    ibuf.append(d)
                    cur_size = cur_size + 1
except EOFError:
    if(len(ibuf) != 0):
        key = ibuf[0x2b]
        frames.append((key, copy.deepcopy(ibuf)))
    pass

# frames.sort()
print(len(frames))

out = open('dmp.opus', 'wb')

import decrypt

for f in frames:
    fi = b''
    if(f[0] == 0x7f): continue
    for d in f[1][0x36:]:
        fi = fi + d.to_bytes(1, 'little')
    print(decrypt.decrypt_audio_bytes(fi))

# flag{BigBrotherIsWatchingYou!!} 
 