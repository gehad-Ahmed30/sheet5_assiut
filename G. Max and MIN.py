def max_min(n, numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    print(f"{min_num} {max_num}")


n = int(input())
numbers = list(map(int, input().split()))
max_min(n, numbers)
