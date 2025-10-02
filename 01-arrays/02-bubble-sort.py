"""
Array
"""

# Sort an array of numbers

numbers: list[int] = [7, 12, 9, 4, 11]

def bubble_sort(items: list[int]) -> list[int]:
    n = len(items)
    
    for i in range(n - 1):
        for j in range(n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    return items

print(bubble_sort(numbers))