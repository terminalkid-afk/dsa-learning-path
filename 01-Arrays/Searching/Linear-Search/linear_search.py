# Linear Search in Python

"""
Goal: Find the index of a target element in a list.
Algorithm: Iterates through the list and compares each element with the target.
"""

def linear_search(arr, target):
    # Iterate through the list using the index
    for i in range(len(arr)):
        # If the current element matches the target, return its index
        if arr[i] == target:
            return i  # Target found!

    # If the loop finishes without returning, the target is not in the list
    return -1  # Target not found

# --- Usage Example ---
if __name__ == "__main__":
    # Test Case 1: Element exists
    numbers = [10, 20, 30, 40, 50]
    target = 30
    result = linear_search(numbers, target)

    print(f"Searching for {target} in {numbers}...")
    if result != -1:
        print(f"✅ Element found at index: {result}")
    else:
        print("❌ Element not found")

    # Test Case 2: Element does not exist
    target_missing = 100
    result_missing = linear_search(numbers, target_missing)

    print(f"\nSearching for {target_missing} in {numbers}...")
    if result_missing != -1:
        print(f"✅ Element found at index: {result_missing}")
    else:
        print("❌ Element not found")
