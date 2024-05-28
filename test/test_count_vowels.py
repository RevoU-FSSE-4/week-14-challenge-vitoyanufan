# test_count_vowels.py

import pytest
from count_vowels import count_vowels

def test_count_vowels():
    assert count_vowels("hello world") == 3
    assert count_vowels("python") == 1
    assert count_vowels("aeiou") == 5
    assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0

if __name__ == "__main__":
    pytest.main()
