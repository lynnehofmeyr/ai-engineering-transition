def remove_vowels(s):
    """
    Removes all vowels from the input string.

    Args:
        s (str): The string to process.

    Returns:
        str: The string with all vowels removed.
    """
    vowels = "aeiouAEIOU"
    return ''.join([char for char in s if char not in vowels])


if __name__ == "__main__":
    test_input = "Lynne Hofmeyr"
    result = remove_vowels(test_input)
    print(f"Input: {test_input}")
    print(f"Without vowels: {result}")

