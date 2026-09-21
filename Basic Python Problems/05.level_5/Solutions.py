# Q41. Count Words in a Sentence
def count_words(sentence):
    words = sentence.split()
    return len(words)


# Q42. Replace All 'a' with 'e'
def replace_a_with_e(s):
    return s.replace('a', 'e')


# Q43. Check if String Contains a Character
def contains_character(s, ch):
    return ch in s


# Q44. Compare Two Strings (Exact Match)
def compare_strings(s1, s2):
    return s1 == s2


# Q45. Count Digits in a String
def count_digits(s):
    count = 0
    for ch in s:
        if ch.isdigit():
            count += 1
    return count


# Q46. Count Uppercase Letters
def count_uppercase(s):
    count = 0
    for ch in s:
        if ch.isupper():
            count += 1
    return count


# Q47. Count Lowercase Letters
def count_lowercase(s):
    count = 0
    for ch in s:
        if ch.islower():
            count += 1
    return count


# Q48. Remove All Vowels from a String
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in s:
        if ch not in vowels:
            result += ch
    return result


# Q49. Remove All Digits from a String
def remove_digits(s):
    result = ""
    for ch in s:
        if not ch.isdigit():
            result += ch
    return result


# Q50. Toggle Case of Each Character
def toggle_case(s):
    result = ""
    for ch in s:
        if ch.islower():
            result += ch.upper()
        elif ch.isupper():
            result += ch.lower()
        else:
            result += ch
    return result

print("Thank you")