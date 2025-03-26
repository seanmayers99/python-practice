# --------------------------
# 🌀 Palindrome Checker – Loop Version
# --------------------------

def is_palindrome_loop(word):
    """
    Checks if a word is a palindrome using a manual loop comparison.
    """
    for i in range(len(word) // 2):
        if word[i] != word[-(i + 1)]:
            return False
    return True


# --------------------------
# ✂️ Palindrome Checker – Slicing Version
# --------------------------

def is_palindrome_sliced(word):
    """
    Checks if a word is a palindrome using Python's string slicing.
    """
    return word == word[::-1]


# --------------------------
# 🧪 Test Cases
# --------------------------

test_words = ["racecar", "hello", "madam", "Python", "a", ""]

print("Testing is_palindrome_loop:")
for word in test_words:
    print(f"{word}: {is_palindrome_loop(word)}")

print("\nTesting is_palindrome_sliced:")
for word in test_words:
    print(f"{word}: {is_palindrome_sliced(word)}")
