"""
Array
"""

# Find the lowest value

numbers: list[int] = [7, 12, 9, 4, 11]

def find_lowest_value(items: list[int]) -> int:
    lowest_value: int = items[0]

    for value in items[1:]:
        if value < lowest_value:
            lowest_value = value
    
    return lowest_value


print("The lowest value of list of numbers is:", find_lowest_value(numbers))
