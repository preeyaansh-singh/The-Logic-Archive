def Rev_Num(num):
    original_num = num
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    print(original_num + rev)

n = int(input("Enter a Number : "))
Rev_Num (n)
