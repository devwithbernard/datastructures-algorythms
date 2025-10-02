"""
Array
"""

# Sort an array of numbers

numbers: list[int] = [7, 12, 9, 4, 11]

def bubble_sort(items: list[int]) -> list[int]:
    """
    Time complexity: O(n2)
    """
    n = len(items)
    
    for i in range(n - 1):
        swapped = False
        
        for j in range(n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break

    return items

print(bubble_sort(numbers))