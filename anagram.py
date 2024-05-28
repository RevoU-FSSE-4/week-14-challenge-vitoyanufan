# anagram.py

def is_anagram(s1: str, s2: str) -> bool:
    """
    This function checks if the two given strings `s1` and `s2` are anagrams.
    
    Two strings are anagrams if they contain the same characters with the same frequencies,
    ignoring spaces and capitalization.
    
    Args:
    - s1 (str): The first input string.
    - s2 (str): The second input string.
    
    Returns:
    - bool: True if the strings are anagrams, False otherwise.
    
    Examples:
    - is_anagram("Listen", "Silent") should return True
    - is_anagram("hello", "billion") should return False
    """
    # Step 1: Clean the strings by removing non-alphanumeric characters and converting to lowercase
    # Step 2: Compare the character counts of both cleaned strings
    
    # Implement your solution here
    pass

# You can test your function with print statements below
# Example:
# print(is_anagram("Listen", "Silent"))  # Expected output: True
# print(is_anagram("hello", "billion"))  # Expected output: False
