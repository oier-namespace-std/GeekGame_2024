


a = 31
b = 55
c = 89
d = 42
print(a**b / c**d)
print(2**(1/2))

# a(n) = ((3^(n+1) + 1)^(n-1) mod (9^(n+1) - 2)) mod (3^(n+1) - 1). - Joseph M. Shunia, Jun 06 2024
def f(n):
    return (3**(n)+1)**(n-2+1//n)%(9**(n)-2)%(3**(n)-1)-1//n
    # return n(n)
    #print((c**d+a**b)**n, (c**d)**n)
    #return (c**d+a**b)**n //(c**d)**n
    # return ((1+q2)**(n-1)+1)//q2//2
    # return ((c**d+a**b)**(n-1)+(c**d)**(n-1))*c**d//a**b//2//(c**d)**(n-1)
    # return ((1+2**(1/2))**(n-1)+1)//(2**(3/2))
    # return ((195025**(n-1))*80782)//(80782**(n-1)*228486)+(n-1)%2*(n<13)
#(2+x^2)/x
#(2+x^2)/x+(2x)/(2+x^2)
#(2+3x^2)/(2x+x^3)
# sqrt(2) ~ a**b//c**d
# ((c**d+a**b)**(n-1)//c**d**(n-1)+1)*c**d//a**b
# ((c**d+a**b)**(n-1)//c**d**(n-1)+1)*c**d//a**b

# 89 42 31 55 

import math

print((1+math.sqrt(2)) ** 200)

#def f(n):
#    return ((1+2**(1/2))**(n-1)-(-2/5)**(n-1)+1)//2**(3/2)

# (1+sq(2)^(n-1))//sq(2)^3


#def f(n):
#    return ((1+2**(1/2))**(n-1)+1)//2**(3/2)

def test():
    print('test')
    for a in range(2, 100):
        for b in range(2, 100):
            for c in range(2, 100):
                for d in range(2, 100):
                    ra = 2*c**(2*d) / a**(2*b)
                    if(ra > 2): break
                    # print(ra)
                    if(ra >= 0.99999 and ra <= 1.00001):
                        print(a, b, c, d, ra)

# test()

def main():
    a,b=0,1
    maxn=40
    for n in range(1,maxn):
        res=f(n)
        print(f'f   {n} : {res}')
        print(f'ans {n} : {a}')
        # assert res==a
        # if level==3:
        #     assert isinstance(res,int)
        a,b=b,a+2*b

main()