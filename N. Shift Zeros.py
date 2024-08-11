def shif_zeros(n,numbers):
    x=[]
    count=0
    for i in numbers:
        if i !=0:
            x.append(i)
        else:
            count+=1
    
    result=x + [0] * count
    return result

n=int(input())
numbers=list(map(int,input().split()))
print(' '.join(map(str,shif_zeros(n,numbers))))