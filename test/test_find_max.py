# test_find_max.py

import pytest
from find_max import find_max

def test_find_max():
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([-1, -2, -3, -4, -5]) == -1
    assert find_max([0]) == 0
    assert find_max([2, 2, 2, 2]) == 2

if __name__ == "__main__":
    pytest.main()
