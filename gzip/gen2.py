import random
import gzip

def average_bit_count(s):
    # print(s)
    ret = 0
    for c in s:
        # print(c)
        r = int(c)
        while(r > 0):
            # print(r)
            ret += r & 1
            r = r // 2
    # print(ret)
    
    return ret / len(s)
    # return sum(c.bit_count() for c in s) / len(s)

def randBits():
    return random.randint(0x40, 0x47) ^ 22
    while(True):
        z1 = min([random.randint(0, 1) for _ in range(3)])
        z2 = min([random.randint(0, 1) for _ in range(3)])
        z3 = min([random.randint(0, 1) for _ in range(3)])
        z4 = min([random.randint(0, 1) for _ in range(3)])
        z5 = min([random.randint(0, 1) for _ in range(3)])
        z6 = min([random.randint(0, 1) for _ in range(3)])
        z7 = min([random.randint(0, 1) for _ in range(3)])
        r = z1 + 2*z2 + 4*z3 + 8*z4 + 16*z5 + 32*z6 + 64*z7
        if(r >= 0x20 and r <= 0x7e):
            return r

s = ''
for _ in range(1000):
    d = min([randBits() for _ in range(8)])
    s = s + chr(d)


def main():
    text = s
    assert len(text)<=1000
    assert all(0x20<=ord(c)<=0x7e for c in text)
        
    text = [ord(c) for c in text]
    #text = [ord(c) ^ 22 for c in text]

    #print('After xor:')
    #print(text)

    #random.seed('YuanShen')
    #random.shuffle(text)
    
    #text = b'\x1f\x8b\x08\x00\xebh\ng\x11\xff3\x03\x00\x14z\xb8\x1d\x01\x00\x00\x00\x00'
    #text = gzip.decompress(bytes(text))

    #print('Temp text:')
    #print(text)
    
    #print('After shuffle:')
    #print(text)
    
    while(True):
        zipval = gzip.compress(bytes(text))
        # print('After processing:')
        # print(text)
        
        prefix = (zipval + b'\xFF'*256)[:256]
        # print(prefix)
        pc = average_bit_count(prefix)
        
        if pc < 2.5:
            print(text)
            exit(0)
        
        cnt = 0

        while(True):
            i = random.randint(0, 999)
            w = text[i]
            text[i] = random.randint(0x20, 0x7e) ^ 22
            zipval = gzip.compress(bytes(text))
            prefix = (zipval + b'\xFF'*256)[:256]
            ipc = average_bit_count(prefix)
            if(ipc < pc): 
                print('abc: ', ipc)
                break
            elif(cnt > 100 and random.randint(0, 1024) == 0): break
            # elif(random.randint(0, int(2 ** (1000 * (ipc - pc)))) == 0): break
            cnt += 1
            text[i] = w

main()


# res = [64, 120, 64, 54, 64, 55, 64, 59, 32, 33, 33, 54, 64, 102, 111, 121, 36, 64, 111, 52, 64, 64, 67, 123, 64, 33, 111, 64, 93, 120, 64, 41, 111, 111, 36, 54, 64, 120, 64, 59, 54, 59, 64, 40, 46, 124, 64, 34, 33, 32, 65, 64, 124, 33, 64, 87, 111, 64, 87, 64, 64, 33, 65, 92, 64, 64, 40, 64, 52, 64, 111, 33, 111, 111, 33, 124, 32, 64, 60, 64, 64, 35, 34, 42, 64, 44, 121, 87, 87, 120, 33, 81, 34, 123, 124, 33, 34, 87, 39, 34, 33, 120, 36, 39, 89, 44, 65, 64, 65, 54, 59, 111, 64, 111, 64, 120, 36, 32, 64, 124, 94, 34, 64, 36, 124, 64, 92, 59, 33, 124, 34, 41, 54, 64, 94, 41, 89, 111, 36, 64, 64, 92, 53, 32, 64, 64, 59, 64, 121, 70, 64, 87, 69, 111, 33, 69, 64, 64, 39, 36, 64, 39, 120, 33, 121, 92, 54, 33, 42, 65, 34, 64, 34, 97, 42, 36, 64, 93, 64, 64, 65, 36, 64, 35, 64, 124, 32, 44, 36, 64, 33, 33, 34, 32, 64, 38, 64, 121, 64, 111, 32, 39, 64, 64, 32, 111, 54, 33, 32, 32, 124, 64, 33, 64, 33, 124, 33, 39, 33, 87, 120, 64, 120, 34, 123, 33, 38, 111, 64, 44, 64, 33, 36, 64, 120, 33, 32, 54, 34, 39, 32, 64, 67, 65, 121, 54, 87, 33, 33, 33, 96, 54, 34, 64, 64, 124, 64, 39, 111, 124, 64, 64, 126, 33, 94, 52, 33, 121, 64, 33, 39, 59, 124, 59, 33, 35, 33, 64, 65, 32, 59, 35, 64, 33, 98, 33, 57, 59, 36, 33, 64, 36, 39, 121, 64, 64, 64, 36, 36, 87, 34, 124, 111, 33, 65, 65, 64, 52, 33, 32, 64, 33, 54, 121, 64, 124, 54, 32, 92, 121, 124, 64, 36, 99, 115, 64, 54, 32, 57, 89, 70, 40, 125, 89, 59, 40, 91, 58, 88, 38, 120, 70, 68, 108, 51, 84, 121, 75, 64, 55, 72, 79, 120, 63, 119, 125, 100, 54, 64, 115, 54, 50, 108, 50, 54, 49, 58, 46, 119, 64, 77, 51, 94, 122, 118, 99, 94, 68, 85, 90, 55, 56, 119, 123, 111, 65, 64, 33, 120, 46, 70, 117, 40, 41, 105, 34, 65, 92, 57, 100, 87, 67, 74, 88, 80, 51, 95, 109, 59, 105, 65, 64, 32, 46, 120, 121, 108, 87, 37, 55, 126, 64, 55, 89, 81, 51, 76, 64, 80, 81, 64, 121, 40, 46, 65, 92, 115, 112, 89, 58, 64, 63, 121, 126, 90, 104, 47, 84, 61, 115, 75, 46, 38, 45, 95, 82, 105, 98, 103, 52, 54, 74, 60, 32, 106, 35, 86, 67, 51, 51, 102, 108, 45, 34, 62, 105, 97, 78, 103, 52, 53, 110, 70, 88, 64, 63, 88, 82, 50, 75, 56, 70, 51, 107, 97, 33, 44, 59, 66, 87, 100, 121, 121, 99, 106, 49, 95, 44, 35, 33, 116, 121, 91, 75, 103, 54, 57, 48, 38, 98, 94, 105, 59, 56, 50, 90, 78, 44, 43, 64, 73, 80, 62, 117, 126, 120, 126, 97, 39, 121, 52, 88, 80, 40, 100, 105, 40, 58, 64, 54, 42, 91, 48, 51, 57, 33, 104, 112, 109, 53, 69, 126, 99, 67, 89, 38, 116, 123, 124, 49, 70, 75, 64, 105, 75, 92, 120, 66, 121, 41, 91, 69, 92, 125, 46, 66, 83, 42, 80, 86, 44, 120, 87, 81, 88, 67, 81, 119, 35, 49, 124, 122, 92, 103, 67, 95, 39, 72, 108, 115, 47, 60, 89, 75, 97, 68, 71, 122, 95, 103, 64, 114, 46, 59, 125, 45, 115, 65, 107, 65, 106, 121, 124, 101, 63, 52, 120, 41, 106, 57, 46, 96, 58, 67, 100, 94, 50, 108, 38, 93, 116, 122, 72, 77, 73, 37, 87, 126, 107, 39, 74, 106, 64, 110, 120, 64, 70, 125, 84, 67, 53, 51, 120, 102, 48, 67, 98, 33, 66, 59, 63, 34, 121, 61, 112, 32, 88, 73, 82, 60, 85, 35, 70, 114, 74, 79, 43, 70, 42, 52, 93, 53, 98, 122, 38, 61, 101, 113, 126, 74, 61, 43, 126, 39, 73, 65, 54, 69, 89, 65, 65, 111, 71, 64, 90, 67, 59, 121, 66, 88, 64, 59, 104, 86, 41, 89, 59, 45, 86, 58, 90, 64, 64, 101, 109, 42, 118, 107, 34, 85, 65, 73, 64, 51, 108, 84, 54, 122, 126, 59, 50, 97, 98, 85, 55, 74, 89, 115, 41, 89, 124, 39, 42, 120, 120, 50, 97, 90, 61, 67, 88, 126, 117, 42, 92, 104, 49, 80, 38, 88, 115, 101, 83, 118, 49, 121, 66, 101, 48, 64, 110, 80, 65, 97, 96, 93, 33, 32, 74, 51, 105, 119, 122, 65, 111, 40, 118, 126, 105, 109, 74, 105, 52, 109, 54, 74, 67, 90, 122, 48, 64, 82, 33, 60, 55, 95, 71, 40, 88, 94, 126, 44, 123, 32, 90, 48, 53, 46, 72, 43, 117, 36, 111, 120, 45, 39, 79, 57, 67, 81, 61, 100, 105, 64, 35, 60, 87, 49, 117, 35, 65, 124, 54, 73, 33, 98, 125, 94, 71, 49, 80, 72, 100, 52, 94, 93, 59, 124, 67, 72, 75, 46, 93, 64, 60, 74, 63, 64, 71, 54, 76, 40, 121, 76, 113, 32, 73, 124, 74, 73, 82, 94, 32, 65, 83, 108, 43, 97, 44, 33, 62, 66, 95, 85, 69, 105, 38, 48, 70, 110, 54, 50, 106, 101, 90, 60, 86, 97, 66, 113, 113, 90, 60, 95, 105, 123, 44, 116, 104, 121, 47, 59, 51, 74, 49, 70, 111, 116, 109, 38, 102, 123, 76, 38, 67, 102, 40, 91, 38, 114, 53, 62, 76, 124, 78, 43, 46, 77, 65, 61, 64, 47, 55, 82, 65, 74, 55, 68, 87, 109, 35, 108, 116, 75, 97, 108, 88, 103, 43, 102]