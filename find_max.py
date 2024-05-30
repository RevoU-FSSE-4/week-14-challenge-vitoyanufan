# find_max.py

def find_max(numbers: list) -> int:
    """
    This function takes a list of numbers and returns the largest number in the list.

    Args:
    - numbers (list): A list of numbers.

    Returns:
    - int: The largest number in the list.

    Examples:
    - find_max([1, 2, 3, 4, 5]) should return 5
    - find_max([-1, -2, -3, -4, -5]) should return -1
    """
    # Implement your solution here
    if not numbers:
        return None  # Jika list kosong, kembalikan None

    # Bubble sort untuk mengurutkan list secara ascending secara manual
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    # Ambil elemen terakhir, yang akan menjadi nilai tertinggi setelah pengurutan
    return numbers[-1]


print(find_max([1, 2, 3, 4, 5]))
print(find_max([-1, -2, -3, -4, -5]))

pass

# You can test your function with print statements below
# Example:
# print(find_max([1, 2, 3, 4, 5]))  # Expected output: 5
# print(find_max([-1, -2, -3, -4, -5]))  # Expected output: -1
