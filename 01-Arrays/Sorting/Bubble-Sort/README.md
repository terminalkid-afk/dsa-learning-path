# Bubble Sort

## 💡 Concept
Bubble Sort is one of the simplest sorting algorithms. It works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order.

The pass through the list is repeated until the list is sorted. The algorithm gets its name because the largest elements "bubble up" to their correct position at the end of the list with each iteration.

**Imagine this:** You are lining up students by height. You look at the first two; if the first is taller, you swap them. Then you look at the second and third, and so on. After one full pass, the tallest person is guaranteed to be at the very end.

### Why do we need it?
- It is a great educational tool to understand the concept of sorting.
- It is stable (does not change the relative order of elements with equal values).
- It can detect if a list is already sorted very quickly.

## ⚙️ Visual Logic
**📺 See it in Action**: [Visualize Bubble Sort here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

Suppose we have an array `[5, 1, 4, 2]`.

**First Pass:**
1. Compare `5` and `1` $\rightarrow$ `5 > 1`, so **Swap**: `[1, 5, 4, 2]`
2. Compare `5` and `4` $\rightarrow$ `5 > 4`, so **Swap**: `[1, 4, 5, 2]`
3. Compare `5` and `2` $\rightarrow$ `5 > 2`, so **Swap**: `[1, 4, 2, 5]`
*End of first pass: The largest element `5` has bubbled to the end.*

**Second Pass:**
1. Compare `1` and `4` $\rightarrow$ `1 < 4`, No swap.
2. Compare `4` and `2` $\rightarrow$ `4 > 2`, so **Swap**: `[1, 2, 4, 5]`
*End of second pass: `4` is now in its correct place.*

## ⏱️ Complexity Analysis

| Case | Time Complexity | Why? |
| :--- | :--- | :--- |
| **Best Case** | $O(n)$ | The list is already sorted (using an optimized flag). |
| **Worst Case** | $O(n^2)$ | The list is sorted in reverse order. |
| **Average Case** | $O(n^2)$ | Two nested loops are required to fully sort the list. |

**Space Complexity:** $O(1)$ as it sorts the array in-place.

## 💻 Implementation

Check out the [bubble_sort.py](./bubble_sort.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Sort an Array](https://leetcode.com/problems/sort-an-array/) (Try implementing Bubble Sort here!)
- [GeeksforGeeks: Bubble Sort](https://www.geeksforgeeks.org/bubble-sort/)
