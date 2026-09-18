# level2_loops_answers.py
# Q11 - Q20 (Loops & Calculations)

def q11_print_1_to_10():
    print("Q11 — Print 1 to 10:")
    for i in range(1, 11):
        print(i, end=" ")
    print("\n")


def q12_print_1_to_n():
    print("Q12 — Print 1 to N:")
    N = 5
    for i in range(1, N + 1):
        print(i, end=" ")
    print("\n")


def q13_even_numbers():
    print("Q13 — Even Numbers 1 to N:")
    N = 10
    for i in range(1, N + 1):
        if i % 2 == 0:
            print(i, end=" ")
    print("\n")


def q14_odd_numbers():
    print("Q14 — Odd Numbers 1 to N:")
    N = 10
    for i in range(1, N + 1):
        if i % 2 != 0:
            print(i, end=" ")
    print("\n")


def q15_sum_1_to_n():
    print("Q15 — Sum 1 to N:")
    N = 5
    total = 0
    for i in range(1, N + 1):
        total += i
    print(total)
    print()


def q16_product_1_to_n():
    print("Q16 — Product 1 to N:")
    N = 4
    product = 1
    for i in range(1, N + 1):
        product *= i
    print(product)
    print()


def q17_multiplication_table():
    print("Q17 — Multiplication Table:")
    n = 5
    for i in range(1, 11):
        print(n * i, end=" ")
    print("\n")


def q18_count_divisible_by_3():
    print("Q18 — Count Numbers Divisible by 3:")
    N = 10
    count = 0
    for i in range(1, N + 1):
        if i % 3 == 0:
            count += 1
    print(count)
    print()


def q19_factorial():
    print("Q19 — Factorial:")
    N = 5
    fact = 1
    for i in range(1, N + 1):
        fact *= i
    print(fact)
    print()


def q20_multiples_of_7():
    print("Q20 — First N Multiples of 7:")
    N = 5
    for i in range(1, N + 1):
        print(7 * i, end=" ")
    print("\n")


if __name__ == "__main__":
    q11_print_1_to_10()
    q12_print_1_to_n()
    q13_even_numbers()
    q14_odd_numbers()
    q15_sum_1_to_n()
    q16_product_1_to_n()
    q17_multiplication_table()
    q18_count_divisible_by_3()
    q19_factorial()
    q20_multiples_of_7()