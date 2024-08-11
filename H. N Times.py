def times(x,y):
    print(' '.join([y] * x))


n=int(input())
for i in range(n):
    x,y=input().split()
    x=int(x)
    times(x,y)