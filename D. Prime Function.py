#from module import is_prime

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

import sys 
input=sys.stdin.read  #"4 3 1\n1 2 3 -5\n-5 4 0 3\n7 7 1 2\n40 6 5 11\n"
n=input().split()

a=int(n[0])
result=[]

for i in range(1, a + 1):
        N = int(n[i])
        if is_prime(N):
            result.append("YES")
        else:
            result.append("NO")
    
print("\n".join(result))




