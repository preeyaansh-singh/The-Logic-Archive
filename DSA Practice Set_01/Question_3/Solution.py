def missing_num (lis):
    a = lis[-1]
    new_lis = [num for num in range(1,a+1)]
    for i in range (0,len(lis)):
        if lis[i] == new_lis[i]:
            continue
        else:
            return(new_lis[i])

array = list(map(int, input("Enter numbers by giving spaces between : ").split()))
print (missing_num(array))