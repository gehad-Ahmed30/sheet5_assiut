def print_num(n):
    list_num=[]
    for i in range(1,n+1):
        list_num.append(i)
    print(' '.join(map(str,list_num)))

n=int(input())
print_num(n)