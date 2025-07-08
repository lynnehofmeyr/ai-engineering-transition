def reverse_string(s):
    """
    Reverses the input string and returns it.
    
    Args:
        s (str): The string to reverse.
    
    Returns:
        str: The reversed string.
    """
    return s[::-1]

# Test the function
if __name__ == "__main__":
    test_input = "lynne"
    result = reverse_string(test_input)
    print(f"Input: {test_input}")
    print(f"Reversed: {result}")

