# Selection Sort in Python

"""
Goal: Sort a list of numbers in ascending order.
Algorithm: Find the minimum element from the unsorted part and put it at the beginning.
"""

def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Assume the current index is the minimum
        min_idx = i

        # Scan the remaining unsorted part to find the actual minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# --- Usage Example ---
if __name__ == "__main__":
    # Test Case 1: Unsorted list
    numbers = [64, 25, 12, 22, 11]
    print(f"Original array: {numbers}")
    sorted_numbers = selection_sort(numbers.copy())
    print(f"Sorted array:   {sorted_numbers}")

    # Test Case 2: Already sorted list
    sorted_list = [1, 2, 3, 4, 5]
    print(f"\nOriginal array: {sorted_list}")
    result = selection_sort(sorted_list.copy())
    print(f"Sorted array:   {result}")

    # Test Case 3: Reverse sorted list
    reverse_list = [5, 4, 3, 2, 1]
    print(f"\nOriginal array: {reverse_list}")
    result_rev = selection_sort(reverse_list.copy())
    print(f"Sorted array:   {result_rev}")
