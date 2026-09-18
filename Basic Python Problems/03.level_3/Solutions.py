# level3_number_logic_answers.py
# Q21 - Q30 (Number Logic)

def q21_count_digits():
    print("Q21 — Count Digits:")
    n = -98
    num = abs(n)

    if num == 0:
        count = 1
    else:
        count = 0
        while num > 0:
            count += 1
            num //= 10

    print(count)
    print()


def q22_sum_of_digits():
    print("Q22 — Sum of Digits:")
    n = 123
    num = abs(n)
    total = 0

    while num > 0:
        total += num % 10
        num //= 10

    print(total)
    print()


def q23_product_of_digits():
    print("Q23 — Product of Digits:")
    n = 505
    num = abs(n)
    product = 1

    while num > 0:
        product *= num % 10
        num //= 10

    print(product)
    print()


def q24_reverse_number():
    print("Q24 — Reverse Number:")
    n = -321
    num = abs(n)
    rev = 0

    while num > 0:
        rev = rev * 10 + (num % 10)
        num //= 10

    if n < 0:
        rev = -rev

    print(rev)
    print()


def q25_palindrome():
    print("Q25 — Palindrome Number:")
    n = 121
    num = abs(n)
    rev = 0
    temp = num

    while temp > 0:
        rev = rev * 10 + (temp % 10)
        temp //= 10

    print(num == rev)
    print()


def q26_prime_check():
    print("Q26 — Prime Number:")
    n = 17

    if n <= 1:
        print(False)
    else:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        print(is_prime)
    print()


def q27_primes_1_to_n():
    print("Q27 — Primes from 1 to N:")
    N = 10

    for num in range(2, N + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
    print("\n")


def q28_fibonacci():
    print("Q28 — Fibonacci Series:")
    N = 5
    a, b = 0, 1

    for i in range(N):
        print(a, end=" ")
        a, b = b, a + b
    print("\n")


def q29_gcd():
    print("Q29 — GCD:")
    a, b = 12, 18

    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    print(gcd)
    print()


def q30_lcm():
    print("Q30 — LCM:")
    a, b = 4, 6

    lcm = max(a, b)
    while True:
        if lcm % a == 0 and lcm % b == 0:
            print(lcm)
            break
        lcm += 1
    print()


if __name__ == "__main__":
    q21_count_digits()
    q22_sum_of_digits()
    q23_product_of_digits()
    q24_reverse_number()
    q25_palindrome()
    q26_prime_check()
    q27_primes_1_to_n()
    q28_fibonacci()
    q29_gcd()
    q30_lcm()
print("Byee yeee")