"""
Array: Insertion sort
"""

numbers: list[int] = [64, 34, 25, 12, 22, 11, 90, 5]


def insertion_sort(items: list[int]) -> list[int]:
    n = len(items)

    for i in range(1, n):
        j = i - 1 
        current_value = items[i]

        while j >= 0 and items[j] > current_value:
            items[j + 1] = items[j]
            j -= 1

        items[j + 1] = current_value

    return items

print("Insertion sort:", insertion_sort(numbers))       

