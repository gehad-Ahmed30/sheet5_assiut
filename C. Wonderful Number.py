def odd_num(n):
    return n % 2 !=0
       
def is_palindrome(n):
    x=bin(n)[2:]         #bin(3) returns '0b11'. 
    return x==x[::-1]

def result(n):
    if odd_num(n) and is_palindrome(n):
        print("YES")
    else:
        print("NO")


n=int(input())
result(n)