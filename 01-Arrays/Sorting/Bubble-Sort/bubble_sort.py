# Bubble Sort in Python

"""
Goal: Sort a list of numbers in ascending order.
Algorithm: Repeatedly swap adjacent elements if they are in the wrong order.
"""

def bubble_sort(arr):
    n = len(arr)

    # Outer loop to traverse through all array elements
    for i in range(n):
        # Flag to track if any swap happened in this pass
        # If no swaps happen, the array is already sorted
        swapped = False

        # Inner loop for adjacent comparisons
        # Last i elements are already in place, so we go up to n-i-1
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Optimization: If no two elements were swapped by inner loop, then break
        if not swapped:
            break

    return arr

# --- Usage Example ---
if __name__ == "__main__":
    # Test Case 1: Unsorted list
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {numbers}")
    sorted_numbers = bubble_sort(numbers.copy())
    print(f"Sorted array:   {sorted_numbers}")

    # Test Case 2: Already sorted list (Tests optimization)
    sorted_list = [1, 2, 3, 4, 5]
    print(f"\nOriginal array: {sorted_list}")
    result = bubble_sort(sorted_list.copy())
    print(f"Sorted array:   {result}")

    # Test Case 3: Reverse sorted list (Worst case)
    reverse_list = [5, 4, 3, 2, 1]
    print(f"\nOriginal array: {reverse_list}")
    result_rev = bubble_sort(reverse_list.copy())
    print(f"Sorted array:   {result_rev}")
