def group(lis):
    even = [num for num in lis if num % 2 == 0]
    odd = [num for num in lis if num % 2 != 0]

    return even + odd

array = list(map(int,input("Enter numbers by giving spaces : ").split()))
print(group(array))
