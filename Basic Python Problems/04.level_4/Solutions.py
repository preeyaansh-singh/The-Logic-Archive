# Q31. Length of String
def string_length(s):
    return len(s)


# Q32. Print Each Character on New Line
def print_chars(s):
    for ch in s:
        print(ch)


# Q33. Count Vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


# Q34. Count Consonants
def count_consonants(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch.isalpha() and ch not in vowels:
            count += 1
    return count


# Q35. To Uppercase
def to_uppercase(s):
    return s.upper()


# Q36. To Lowercase
def to_lowercase(s):
    return s.lower()


# Q37. Reverse a String
def reverse_string(s):
    return s[::-1]


# Q38. Palindrome String
def is_palindrome(s):
    return s == s[::-1]


# Q39. Count Occurrences of 'a'
def count_a(s):
    count = 0
    for ch in s:
        if ch == 'a' or ch == 'A':
            count += 1
    return count


# Q40. Remove All Spaces
def remove_spaces(s):
    return s.replace(" ", "")