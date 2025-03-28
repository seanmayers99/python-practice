def reverse_string(word):
    # Start with an empty string that will hold the reversed version
    reversed_str = ""
    
    # Print the original word (for visualization)
    print(f"Original word: {word}")

    # Loop through the original string backwards using index
    for i in range(len(word) - 1, -1, -1):
        # Print the character being added to the result
        print(f"Adding '{word[i]}' to reversed_str")

        # Append the current character to the reversed string
        reversed_str += word[i]

        # Print the current state of the reversed string
        print(f"Current reversed_str: {reversed_str}")

    # Final print before returning the result
    print(f"Final reversed word: {reversed_str}")
    
    # Return the fully reversed string
    return reversed_str


# 🧪 Test the function with a few examples
reverse_string("cat")
print("\n")
reverse_string("Sean")
print("\n")
reverse_string("Python")
