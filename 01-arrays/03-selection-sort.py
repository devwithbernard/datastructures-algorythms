"""
Array: Selection sort
"""

numbers: list[int] = [64, 34, 25, 5, 22, 11, 90, 12]

def selection_sort(items: list[int]) -> list[int]:
    """
    Time complexity: O(n2)
    """
    n = len(items)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if items[j] < items[min_index]:
                min_index = j
        
        items[i], items[min_index] = items[min_index], items[i]

    return items

print("After selection sort:", selection_sort(numbers))
