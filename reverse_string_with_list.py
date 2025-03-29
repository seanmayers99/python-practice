def reverse_string_with_list(word):
    """
    Reverses a string using a list and join() instead of string concatenation.
    This is more efficient for longer strings.
    """
    chars = []  # Create an empty list to collect characters

    # Loop through the string backwards
    for i in range(len(word) - 1, -1, -1):
        chars.append(word[i])  # Append each character to the list

    # Join all characters in the list into a single reversed string
    return ''.join(chars)


# 🧪 Test cases to validate the function
print(reverse_string_with_list("cat"))     # Expected: "tac"
print(reverse_string_with_list("Sean"))    # Expected: "naeS"
print(reverse_string_with_list("Python"))  # Expected: "nohtyP"
