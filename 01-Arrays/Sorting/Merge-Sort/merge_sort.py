# Merge Sort in Python

"""
Goal: Sort a list of numbers in ascending order.
Algorithm: Divide the list into halves recursively and then merge them in sorted order.
"""

def merge_sort(arr):
    # Base case: A list with 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    # 1. DIVIDE: Find the middle point
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    merge_sort(left_half)
    merge_sort(right_half)

    # 2. CONQUER: Merge the two sorted halves back together
    i = j = k = 0

    # Compare elements from both halves and place the smaller one into the main array
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # If there are remaining elements in left_half, add them
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # If there are remaining elements in right_half, add them
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

    return arr

# --- Usage Example ---
if __name__ == "__main__":
    # Test Case 1: Unsorted list
    numbers = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original array: {numbers}")
    sorted_numbers = merge_sort(numbers.copy())
    print(f"Sorted array:   {sorted_numbers}")

    # Test Case 2: Already sorted list
    sorted_list = [1, 2, 3, 4, 5]
    print(f"\nOriginal array: {sorted_list}")
    result = merge_sort(sorted_list.copy())
    print(f"Sorted array:   {result}")

    # Test Case 3: Reverse sorted list
    reverse_list = [5, 4, 3, 2, 1]
    print(f"\nOriginal array: {reverse_list}")
    result_rev = merge_sort(reverse_list.copy())
    print(f"Sorted array:   {result_rev}")
