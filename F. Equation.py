def equation(x,y):
    result=0
    for i in range(2,y+1):
        if i % 2==0:
          result+=(x ** i)
    return result

x,y=map(int,input().split())
print(equation(x,y))