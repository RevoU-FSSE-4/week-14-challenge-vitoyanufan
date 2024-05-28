# test_fizzbuzz.py

import pytest
from fizzBuzz import fizzbuzz

def test_fizzbuzz():
    assert fizzbuzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizzbuzz(1) == ["1"]
    assert fizzbuzz(0) == []

if __name__ == "__main__":
    pytest.main()
