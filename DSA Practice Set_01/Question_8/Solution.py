def first_non_repeating(text):
    counts = {}

    for character in text:
        counts[character] = counts.get(character, 0) + 1

    for character in text:
        if counts[character] == 1:
            return character

    return None


text = input("Enter a string: ")
result = first_non_repeating(text)
print(result if result is not None else "No non-repeating character found")
