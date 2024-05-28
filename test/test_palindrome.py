# test_palindrome.py

from palindrome import is_palindrome

def test_palindrome_with_punctuation():
    assert is_palindrome("A man, a plan, a canal, Panama") == True
    
def test_simple_palindrome():
    assert is_palindrome("racecar") == True
    
def test_not_palindrome():
    assert is_palindrome("hello") == False
    
def test_empty_string():
    assert is_palindrome("") == True  # An empty string is considered a palindrome
    
def test_single_character():
    assert is_palindrome("a") == True  # A single character is considered a palindrome
    
def test_mixed_case():
    assert is_palindrome("Able was I ere I saw Elba") == True

# if __name__ == "__main__":
#     pytest.main()

# To run the tests, use the command:
# pytest test_palindrome.py
