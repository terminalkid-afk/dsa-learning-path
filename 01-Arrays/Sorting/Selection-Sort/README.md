# Selection Sort

## 💡 Concept
Selection Sort is a simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the list and placing it at the beginning.

The algorithm maintains two sub-arrays in a given array:
1. The sorted part (initially empty).
2. The unsorted part (initially the entire array).

In every iteration, the smallest element from the unsorted part is "selected" and swapped with the leftmost element of the unsorted part, effectively expanding the sorted part.

**Imagine this:** You have a pile of unsorted cards. You scan the whole pile for the smallest card, pick it up, and place it on a new pile. You repeat this until the first pile is empty and the second pile is perfectly sorted.

### Why do we need it?
- It is very simple to understand and implement.
- It performs the minimum number of swaps possible ($O(n)$ swaps), which is useful if swapping is an expensive operation (like writing to flash memory).

## ⚙️ Visual Logic
**📺 See it in Action**: [Visualize Selection Sort here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

Suppose we have an array `[64, 25, 12, 22, 11]`.

**First Pass:**
1. Scan the whole list to find the minimum. Minimum is `11`.
2. Swap `11` with the first element `64`.
3. Array becomes: `[11, 25, 12, 22, 64]`

**Second Pass:**
1. Scan the remaining unsorted part `[25, 12, 22, 64]` for the minimum. Minimum is `12`.
2. Swap `12` with the first unsorted element `25`.
3. Array becomes: `[11, 12, 25, 22, 64]`

...and so on until the entire array is sorted.

## ⏱️ Complexity Analysis

| Case | Time Complexity | Why? |
| :--- | :--- | :--- |
| **Best Case** | $O(n^2)$ | Even if sorted, it still scans the rest of the array to find the minimum. |
| **Worst Case** | $O(n^2)$ | Two nested loops are required. |
| **Average Case** | $O(n^2)$ | Standard nested loop behavior. |

**Space Complexity:** $O(1)$ as it is an in-place sorting algorithm.

## 💻 Implementation

Check out the [selection_sort.py](./selection_sort.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Sort an Array](https://leetcode.com/problems/sort-an-array/)
- [GeeksforGeeks: Selection Sort](https://www.geeksforgeeks.org/selection-sort/)
