def distinct_num(n,number):
    x=set(number)
    
    return len(x)

n=int(input())
number=list(map(int,input().split()))
print(distinct_num(n,number))