# Binary Search in Python

"""
Goal: Find the index of a target element in a SORTED list.
Algorithm: Repeatedly divide the search interval in half.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Find the middle index
        mid = (low + high) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid  # Target found!

        # If target is smaller, ignore the right half
        elif arr[mid] > target:
            high = mid - 1

        # If target is larger, ignore the left half
        else:
            low = mid + 1

    # Target is not present in the array
    return -1

# --- Usage Example ---
if __name__ == "__main__":
    # IMPORTANT: The list MUST be sorted for Binary Search to work
    numbers = [10, 20, 30, 40, 50, 60, 70]

    # Test Case 1: Element exists
    target = 60
    result = binary_search(numbers, target)

    print(f"Searching for {target} in sorted list {numbers}...")
    if result != -1:
        print(f"✅ Element found at index: {result}")
    else:
        print("❌ Element not found")

    # Test Case 2: Element does not exist
    target_missing = 25
    result_missing = binary_search(numbers, target_missing)

    print(f"\nSearching for {target_missing} in sorted list {numbers}...")
    if result_missing != -1:
        print(f"✅ Element found at index: {result_missing}")
    else:
        print("❌ Element not found")
