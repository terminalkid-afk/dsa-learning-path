# Quick Sort in Python

"""
Goal: Sort a list of numbers in ascending order.
Algorithm: Divide and Conquer using a Pivot to partition the array.
"""

def quick_sort(arr):
    # Base case: Arrays with 0 or 1 elements are already sorted
    if len(arr) <= 1:
        return arr

    # We pick the middle element as the pivot to avoid O(n^2) on sorted lists
    pivot = arr[len(arr) // 2]

    # Partitioning the array into three lists
    # Elements smaller than the pivot
    left = [x for x in arr if x < pivot]
    # Elements equal to the pivot
    middle = [x for x in arr if x == pivot]
    # Elements larger than the pivot
    right = [x for x in arr if x > pivot]

    # Recursively sort the left and right parts, then combine them
    return quick_sort(left) + middle + quick_sort(right)

# --- Usage Example ---
if __name__ == "__main__":
    # Test Case 1: Unsorted list
    numbers = [10, 80, 30, 90, 40, 50, 70]
    print(f"Original array: {numbers}")
    sorted_numbers = quick_sort(numbers.copy())
    print(f"Sorted array:   {sorted_numbers}")

    # Test Case 2: Already sorted list
    sorted_list = [1, 2, 3, 4, 5]
    print(f"\nOriginal array: {sorted_list}")
    result = quick_sort(sorted_list.copy())
    print(f"Sorted array:   {result}")

    # Test Case 3: Reverse sorted list
    reverse_list = [5, 4, 3, 2, 1]
    print(f"\nOriginal array: {reverse_list}")
    result_rev = quick_sort(reverse_list.copy())
    print(f"Sorted array:   {result_rev}")
