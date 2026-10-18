# Insertion Sort in Python

"""
Goal: Sort a list of numbers in ascending order.
Algorithm: Build the sorted array one item at a time by inserting elements into their correct position.
"""

def insertion_sort(arr):
    # Traverse from the second element to the end
    for i in range(1, len(arr)):
        key = arr[i]  # The element we want to insert
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than the key
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key in its correct sorted position
        arr[j + 1] = key

    return arr

# --- Usage Example ---
if __name__ == "__main__":
    # Test Case 1: Unsorted list
    numbers = [12, 11, 13, 5, 6]
    print(f"Original array: {numbers}")
    sorted_numbers = insertion_sort(numbers.copy())
    print(f"Sorted array:   {sorted_numbers}")

    # Test Case 2: Already sorted list (Best case)
    sorted_list = [1, 2, 3, 4, 5]
    print(f"\nOriginal array: {sorted_list}")
    result = insertion_sort(sorted_list.copy())
    print(f"Sorted array:   {result}")

    # Test Case 3: Reverse sorted list (Worst case)
    reverse_list = [5, 4, 3, 2, 1]
    print(f"\nOriginal array: {reverse_list}")
    result_rev = insertion_sort(reverse_list.copy())
    print(f"Sorted array:   {result_rev}")
