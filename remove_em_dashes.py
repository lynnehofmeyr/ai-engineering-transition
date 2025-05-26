def remove_em_dashes(s):
    """
    Removes all em dashes (—) from the input string.

    Args:
        s (str): The string to clean.

    Returns:
        str: The string with all em dashes removed.
    """
    return s.replace("—", "")


if __name__ == "__main__":
    test_input = "This sentence—contains—em dashes."
    result = remove_em_dashes(test_input)
    print(f"Input: {test_input}")
    print(f"Cleaned: {result}")

