"""
Array: Linear search
Time complexity: O(n)
"""

def linear_search(arr: list[int], target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return -1

numbers: list[int] = [64, 34, 25, 12, 22, 11, 90, 5]

print("Not found" if linear_search(numbers, 25) == -1 else f"Found a index: {linear_search(numbers, 25)}")