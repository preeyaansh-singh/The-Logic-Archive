def prime_between(start, end):
    if start > end:
        start, end = end, start

    primes = []

    for number in range(start, end + 1):
        if number < 2:
            continue

        is_prime = True

        for divisor in range(2, number):
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(number)

    return primes


num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number greater than the previous one: "))
print(prime_between(num_1, num_2))


