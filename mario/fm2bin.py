for _ in range(17): input()

try:
    with open('out.bin', 'wb') as buf:
        while(True):
            s = input()
            s = s[3:11]
            ret = 0
            for i,w in enumerate(s):
                if(w != '.'):
                    ret += (128 >> i)
            print(s, ret)
            buf.write(ret.to_bytes(1, 'little'))
except EOFError:
    pass

# task 1 https://tasvideos.org/1330M src=klmz3-smb.fm2
# task 1 flag{our-princess-is-in-an0th3r-castle}


# task 2 https://tasvideos.org/UserFiles/Info/638619947992862452 src=-1.fm2
# task 2 flag{Nintendo-rul3d-the-fxxking-w0rld}

