import math

def sim(n):
    ret = 0
    while(n >= 100):
        cache = 0
        bi = 0
        ki = 0
        # print(n)
        for k in range(2, 1000):
            b = int((n ** (1 / k)))
            if(b > 2000): continue
            if(b ** k > n): continue
            if(b ** k > cache):
                cache = b ** k
                bi, ki = b, k
        n -= cache
        ret += 6
    return ret

def simlog(n):
    ret = 0
    while(n >= 100000000):
        cache = 0
        bi = 0
        ki = 0
        # print(n)
        for k in range(10, 1000):
            b = int((n ** (1 / k)))
            if(b > 2000): continue
            if(b ** k > n): continue
            if(b ** k > cache):
                cache = b ** k
                bi, ki = b, k
        print(f'{bi}**{ki}+', end = '')
        n -= cache
        ret += 6
    print(f'{n}')
    return ret


n = 1643489790079051446594178525504912537670557559936044099205162721893035638970193795282183888721142563635467015861974791565738697561363611450442116638892
rb = 100000
while(True):
    r = sim(n)
    if(rb > r):
        rb = r
        print(r, n)
        simlog(n)
    if(r <= 42):
        print(n)
        exit(0)
    n += 2 ** 500
