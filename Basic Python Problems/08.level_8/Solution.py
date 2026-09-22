# Q71. Remove Even Numbers (Keep Only Odd)
def remove_even(arr):
    return [x for x in arr if x % 2 != 0]


# Q72. Remove Duplicates (Preserve Order)
def remove_duplicates(arr):
    seen = set()
    result = []
    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


# Q73. Concatenate Two Arrays
def concatenate_arrays(arr1, arr2):
    return arr1 + arr2


# Q74. Intersection of Two Arrays (No Duplicates)
def intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))


# Q75. Rotate Array Right by 1
def rotate_right(arr):
    if not arr:
        return arr
    return [arr[-1]] + arr[:-1]


# Q76. Rotate Array Left by 1
def rotate_left(arr):
    if not arr:
        return arr
    return arr[1:] + [arr[0]]


# Q77. Count Elements Greater than Average
def count_greater_than_avg(arr):
    if not arr:
        return 0
    avg = sum(arr) / len(arr)
    count = 0
    for x in arr:
        if x > avg:
            count += 1
    return count


# Q78. Largest Positive and Smallest Negative
def pos_neg_values(arr):
    largest_pos = None
    smallest_neg = None
    
    for x in arr:
        if x > 0:
            if largest_pos is None or x > largest_pos:
                largest_pos = x
        elif x < 0:
            if smallest_neg is None or x < smallest_neg:
                smallest_neg = x
                
    return largest_pos, smallest_neg


# Q79. Count 0s and 1s in Binary Array
def count_binary(arr):
    zeros = 0
    ones = 0
    
    for x in arr:
        if x == 0:
            zeros += 1
        elif x == 1:
            ones += 1
            
    return zeros, ones


# Q80. Separate Even and Odd into Two Arrays
def separate_even_odd(arr):
    evens = []
    odds = []
    
    for x in arr:
        if x % 2 == 0:
            evens.append(x)
        else:
            odds.append(x)
            
    return evens, odds