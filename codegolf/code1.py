def f(n):
    # return 665772//2**n%2+(n%2*n%3*n%5*n%7*n%11*n%13*n%17*n%19+98)//99
    # return n**1658880%9699690
    return 665772//2**n%2+(9**9+2-n**1658880%9699690)//9**9
    return 665772//2**n%2+(9**9+n%19-n**92160%510510)//9**9
    
    
    
#    ((15**(n-1))%n==1)

for i in range(2, 100):
    print(f(i))

primes=list(range(2,500))
for j in primes[:]:
    primes=[i for i in primes if i<=j or i%j!=0]

x = 0
for i in range(20):
    if i in primes:
        x = x + (1 << i)

print(x)

