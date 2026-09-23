# Q1. Positive Number and Even/Odd
n = int(input())

if n > 0:
    if n % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Not Positive")


# Q2. Age Eligibility
age = int(input())

if age >= 18:
    if age >= 60:
        print("Senior Eligible")
    else:
        print("Adult Eligible")
else:
    print("Not Eligible")


# Q3. Marks and Pass Category
marks = int(input())

if marks >= 40:
    if marks >= 75:
        print("Distinction")
    else:
        print("Pass")
else:
    print("Fail")


# Q4. Number Greater Than 10
n = int(input())

if n > 10:
    if n > 50:
        print("Large Number")
    else:
        print("Medium Number")
else:
    print("10 or Less")