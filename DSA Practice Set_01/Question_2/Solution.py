def second_highest(numbers):
    highest = max(numbers)
    remaining_numbers = [number for number in numbers if number != highest]
    return max(remaining_numbers)
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(second_highest(numbers))


