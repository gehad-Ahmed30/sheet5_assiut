def average(n,numbers):
    summ=0
    for i in numbers:
        summ+=i
    result=summ / n
    return result




n=int(input())
numbers=list(map(float,input().split()))
print(f"{average(n,numbers):.6f}")