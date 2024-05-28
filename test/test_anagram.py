# test_anagram.py

import pytest
from anagram import is_anagram

def test_is_anagram():
    assert is_anagram("Listen", "Silent") == True
    assert is_anagram("hello", "billion") == False
    assert is_anagram("A gentleman", "Elegant man") == True
    assert is_anagram("Clint Eastwood", "Old West action") == True
    assert is_anagram("Dormitory", "Dirty room") == True
    assert is_anagram("School master", "The classroom") == True
    assert is_anagram("Astronomer", "Moon starer") == True
    assert is_anagram("The eyes", "They see") == True
    assert is_anagram("Conversation", "Voices rant on") == True
    assert is_anagram("Listen", "Silent!") == True

if __name__ == "__main__":
    pytest.main()
