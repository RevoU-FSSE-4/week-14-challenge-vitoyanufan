# palindrome.py

def is_palindrome(s: str) -> bool:
    """
    This function checks if the given string `s` is a palindrome.
    
    A palindrome is a word, phrase, number, or other sequence of characters 
    that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
    
    Args:
    - s (str): The input string.
    
    Returns:
    - bool: True if the string is a palindrome, False otherwise.
    
    Examples:
    - is_palindrome("A man, a plan, a canal, Panama") should return True
    - is_palindrome("racecar") should return True
    - is_palindrome("hello") should return False
    """
    def is_lowercase_alpha(char):
        return 'a' <= char <= 'z' or '0' <= char <= '9'

    cleaned_string = ""
    for char in s:
        if is_lowercase_alpha(char.lower()):
            cleaned_string += char.lower()

    left, right = 0, len(cleaned_string) - 1
    while left < right:
        if cleaned_string[left] != cleaned_string[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_palindrome("A man, a plan, a canal, Panama"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))

pass

# You can test your function with print statements below
# Example:
# print(is_palindrome("A man, a plan, a canal, Panama"))  # Expected output: True
# print(is_palindrome("racecar"))  # Expected output: True
# print(is_palindrome("hello"))  # Expected output: False
