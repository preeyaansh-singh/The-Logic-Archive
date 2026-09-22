# Q51. Print All Elements of an Array
def print_elements(arr):
    for x in arr:
        print(x, end=" ")
    print()


# Q52. Sum of Array Elements
def sum_array(arr):
    total = 0
    for x in arr:
        total += x
    return total


# Q53. Maximum in Array
def max_element(arr):
    if not arr:
        return None
    max_val = arr[0]
    for x in arr:
        if x > max_val:
            max_val = x
    return max_val


# Q54. Minimum in Array
def min_element(arr):
    if not arr:
        return None
    min_val = arr[0]
    for x in arr:
        if x < min_val:
            min_val = x
    return min_val


# Q55. Count Even Numbers in Array
def count_even(arr):
    count = 0
    for x in arr:
        if x % 2 == 0:
            count += 1
    return count


# Q56. Count Odd Numbers in Array
def count_odd(arr):
    count = 0
    for x in arr:
        if x % 2 != 0:
            count += 1
    return count


# Q57. Print Only Positive Numbers
def print_positive(arr):
    for x in arr:
        if x > 0:
            print(x, end=" ")
    print()


# Q58. Print Only Negative Numbers
def print_negative(arr):
    for x in arr:
        if x < 0:
            print(x, end=" ")
    print()


# Q59. Print Elements Greater than 10
def print_greater_than_10(arr):
    for x in arr:
        if x > 10:
            print(x, end=" ")
    print()


# Q60. Average of Array Elements
def average_array(arr):
    if not arr:
        return 0
    total = 0
    for x in arr:
        total += x
    return total / len(arr)