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
    def to_lowercase(word):
        lower_word = ""
        for char in word:
            if "A" <= char <= "Z":
                lower_word += chr(ord(char) + 32)
            else:
                lower_word += char
        return lower_word
    
    def is_alphanumeric(char):
        return ('a' <= char <= 'z') or ('0' <= char <= '9')
    
    def word_converter(word):
        convert_word = ''
        for char in word:
            lower_char = to_lowercase(char)
            if is_alphanumeric(lower_char):
                convert_word += lower_char
        return convert_word
    
    s1 = word_converter(s1)
    s2 = word_converter(s2)
    
    if len(s1) != len(s2):
        return False
    
    count = [0] * 26

    for i in range(len(s1)):
        count[ord(s1[i]) - ord('a')] += 1
        count[ord(s2[i]) - ord('a')] -= 1

    for c in count:
        if c != 0:
            return False

    return True

print(is_anagram("Listen", "Silent"))
print(is_anagram("hello", "billion"))

pass

# You can test your function with print statements below
# Example:
# print(is_anagram("Listen", "Silent"))  # Expected output: True
# print(is_anagram("hello", "billion"))  # Expected output: False
