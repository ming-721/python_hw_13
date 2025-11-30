# 과제 39
def print_odd_numbers(n):
    for i in range(1, n+1):
        if i % 2 != 0:
            print(i, end=' ')

num = int(input("양수 입력: "))
print_odd_numbers(num)

# 과제 40
def print_3(n):
    if n % 3 == 0:
        print(n)

num = int(input("숫자 입력: "))
print_3(num)

# 과제 41
def max_min(a, b, c, d):
    nums = [a, b, c, d]
    return max(nums), min(nums)

a,b,c,d = map(int,input("숫자 4개 입력: ").split())
print(max_min(a, b, c, d))

# 과제 42
# 39번 문제와 같습니다.

# 과제 43
def fact(n):
    result = 1
    for i in range (1, n+1):
        result *= i
    return result

a = int(input("정수 n 입력: "))
print(fact(a))

# 과제 44
def sum(i,j):
    result = 0
    for x in range(1,i+1):
        for y in range(1,j+1):
            if x * y >= 30:
                result += x * y
    return result

i,j = map(int, input("2~9 사이 숫자 2개 입력: ").split())
print(sum(i,j))

# 과제 45
def sum(list):
    result = []
    total = 0
    for i in list:
        total += i
        result.append(total)
    return result

a = [1,2,3,4,5]
print(sum(a))