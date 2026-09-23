# Q5. Positive, Negative, or Zero with Even/Odd
n = int(input())

if n > 0:
    if n % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    if n == 0:
        print("Zero")
    else:
        print("Negative")


# Q6. Student Performance
marks = int(input())

if marks >= 40:
    if marks >= 75:
        print("Good Performance")
    else:
        print("Pass")
else:
    if marks >= 30:
        print("Needs Improvement")
    else:
        print("Fail")


# Q7. Shopping Purchase
amount = int(input())

if amount >= 1000:
    if amount >= 5000:
        print("Premium Purchase")
    else:
        print("Regular Purchase")
else:
    if amount > 0:
        print("Small Purchase")
    else:
        print("Invalid Amount")


# Q8. Electricity Usage
units = int(input())

if units > 100:
    if units > 300:
        print("High Usage")
    else:
        print("Medium Usage")
else:
    if units > 0:
        print("Low Usage")
    else:
        print("Invalid Units")