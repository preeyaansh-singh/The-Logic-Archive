# Q81. Square Pattern of *
n = int(input())
for _ in range(n):
    print("* " * n)


# Q82. Right-Angled Triangle of *
n = int(input())
for i in range(1, n + 1):
    print("* " * i)


# Q83. Number Triangle Increasing Each Row
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# Q84. Triangle with Repeated Row Number
n = int(input())
for i in range(1, n + 1):
    print((str(i) + " ") * i)


# Q85. Multiplication Tables from 1 to 10
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()


# Q86. Sum of Each Row in 2D Array
rows = int(input())
matrix = []
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

result = []
for row in matrix:
    total = 0
    for num in row:
        total += num
    result.append(total)

print(result)


# Q87. Check Perfect Square
n = int(input())
i = 0
is_square = False

while i * i <= n:
    if i * i == n:
        is_square = True
        break
    i += 1

print(is_square)


# Q88. Armstrong Number (3-digit)
n = int(input())
temp = n
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp //= 10

print(total == n)


# Q89. Length of Each String in Array
arr = input().split()
result = []

for s in arr:
    result.append(len(s))

print(result)


# Q90. Longest String in Array
arr = input().split()

if len(arr) == 0:
    print("")
else:
    longest = arr[0]
    for s in arr:
        if len(s) > len(longest):
            longest = s
    print(longest)