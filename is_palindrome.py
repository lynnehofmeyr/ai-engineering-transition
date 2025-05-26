def is_palindrome(s):
    """
    Checks if the input string is a palindrome.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    return s == s[::-1]


if __name__ == "__main__":
    test_input = "racecar"
    result = is_palindrome(test_input)
    print(f"Input: {test_input}")
    print(f"Is palindrome? {result}")

