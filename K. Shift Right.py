def swap_num(y,n):
    a=y % len(n)          #x % n. Here, 2 % 5 is still 2
    result=n[-a:] + n[:-a]       #[4, 5] + [1, 2, 3] which gives [4, 5, 1, 2, 3]
    return result


x,y=map(int,input().split())
n=list(map(int,input().split()))
print(f"{' '.join(map(str,swap_num(y,n)))}")