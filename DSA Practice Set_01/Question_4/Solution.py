def frequency_without_counter(items):
    freq = {}

    for item in items:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    return freq


# Example usage
numbers = list(map(int,input("Enter the numbers by giving spaces : ").split()))
print(frequency_without_counter(numbers))
