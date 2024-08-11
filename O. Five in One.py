def max_num(n,numbers):
    maxnum=max(numbers)
    return maxnum


def min_num(n,numbers):
    minnum=min(numbers)
    return minnum

def is_palindrome(numbers):     #convert to string
    x=str(numbers)
    return x==x[::-1]

def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count

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

n=int(input())
numbers=list(map(int,input().split()))

palindrome_count= 0
for num in numbers:
    if is_palindrome(num):
        palindrome_count += 1

prime_count = 0
for num in numbers:
    if is_prime(num):
        prime_count += 1

# Find number with maximum divisors
max_divisors_count = 0
number_with_max_divisors = numbers[0]
for num in numbers:
    divisors_count = count_divisors(num)
    if divisors_count > max_divisors_count:
        max_divisors_count = divisors_count
        number_with_max_divisors = num
    elif divisors_count == max_divisors_count:
        number_with_max_divisors = max(number_with_max_divisors, num)


print(f"The maximum number : {max_num(n,numbers)}")
print(f"The minimum number : {min_num(n,numbers)}")
print(f"The number of prime numbers : {prime_count}")
print(f"The number of palindrome numbers : {palindrome_count}")
print(f"The number that has the maximum number of divisors : {number_with_max_divisors}")
