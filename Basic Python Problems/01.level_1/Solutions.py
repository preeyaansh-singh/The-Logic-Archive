# level1_if_else_answers.py
# Q1 - Q10 (Basics: if-else)

def q1_even_odd():
    print("Q1 — Even or Odd:")
    num = 4
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
    print()


def q2_max_two():
    print("Q2 — Maximum of Two Numbers:")
    a, b = 5, 9
    if a > b:
        print(a)
    else:
        print(b)
    print()


def q3_max_three():
    print("Q3 — Maximum of Three Numbers:")
    a, b, c = 3, 7, 5
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)
    print()


def q4_positive_negative_zero():
    print("Q4 — Positive, Negative, or Zero:")
    num = -2
    if num > 0:
        print("positive")
    elif num < 0:
        print("negative")
    else:
        print("zero")
    print()


def q5_age_group():
    print("Q5 — Age Group:")
    age = 15
    if age <= 12:
        print("child")
    elif age <= 19:
        print("teenager")
    else:
        print("adult")
    print()


def q6_grade_calculator():
    print("Q6 — Grade Calculator:")
    marks = 75
    if marks >= 90:
        print("A")
    elif marks >= 80:
        print("B")
    elif marks >= 70:
        print("C")
    elif marks >= 60:
        print("D")
    else:
        print("F")
    print()


def q7_divisible_by_5():
    print("Q7 — Divisible by 5:")
    num = 11
    if num % 5 == 0:
        print("divisible by 5")
    else:
        print("not divisible by 5")
    print()


def q8_divisible_by_3_and_5():
    print("Q8 — Divisible by 3 and 5:")
    num = 9
    if num % 3 == 0 and num % 5 == 0:
        print("divisible by 3 and 5")
    else:
        print("not divisible by both")
    print()


def q9_leap_year():
    print("Q9 — Leap Year:")
    year = 2021
    if year % 4 == 0:
        print("leap year")
    else:
        print("not a leap year")
    print()


def q10_in_range():
    print("Q10 — In Range 10–50:")
    num = 7
    if 10 <= num <= 50:
        print("in range")
    else:
        print("out of range")
    print()


if __name__ == "__main__":
    q1_even_odd()
    q2_max_two()
    q3_max_three()
    q4_positive_negative_zero()
    q5_age_group()
    q6_grade_calculator()
    q7_divisible_by_5()
    q8_divisible_by_3_and_5()
    q9_leap_year()
    q10_in_range()
    