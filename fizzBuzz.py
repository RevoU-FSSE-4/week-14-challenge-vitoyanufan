# fizzbuzz.py

def fizzbuzz(n: int) -> list:
    """
    This function returns a list of strings with the numbers from 1 to `n`.
    But for multiples of three, return "Fizz" instead of the number and for the multiples of five, return "Buzz".
    For numbers which are multiples of both three and five, return "FizzBuzz".

    Args:
    - n (int): The upper limit of the range (inclusive).

    Returns:
    - list: A list of strings representing the FizzBuzz sequence.
    
    Examples:
    - fizzbuzz(15) should return ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    """
    # Implement your solution here]
    result = []
    i = 1
    while i <= n:
        if i // 3 * 3 == i and i // 5 * 5 == i:
            result.append("FizzBuzz")
        elif i // 3 * 3 == i:
            result.append("Fizz")
        elif i // 5 * 5 == i:
            result.append("Buzz")
        else:
            result.append(str(i))
        i += 1
    return result


print(fizzbuzz(15))


pass

# You can test your function with print statements below
# Example:
# print(fizzbuzz(15))  # Expected output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
