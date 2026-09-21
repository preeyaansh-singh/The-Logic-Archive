# Q61. Double Each Element
def double_elements(arr):
    return [x * 2 for x in arr]


# Q62. Square Each Element
def square_elements(arr):
    return [x ** 2 for x in arr]


# Q63. Reverse Array into New Array
def reverse_array(arr):
    return arr[::-1]


# Q64. Copy Array
def copy_array(arr):
    return arr[:]


# Q65. Check if Array Contains a Value
def contains_value(arr, value):
    return value in arr


# Q66. Find Index of a Value
def find_index(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1


# Q67. Frequency of a Value
def frequency(arr, value):
    count = 0
    for x in arr:
        if x == value:
            count += 1
    return count


# Q68. Check if Array is Sorted (Increasing)
def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True


# Q69. Second Largest Element
def second_largest(arr):
    largest = float('-inf')
    second = float('-inf')
    
    for x in arr:
        if x > largest:
            second = largest
            largest = x
        elif x > second and x != largest:
            second = x
            
    return second


# Q70. Second Smallest Element
def second_smallest(arr):
    smallest = float('inf')
    second = float('inf')
    
    for x in arr:
        if x < smallest:
            second = smallest
            smallest = x
        elif x < second and x != smallest:
            second = x
            
    return second