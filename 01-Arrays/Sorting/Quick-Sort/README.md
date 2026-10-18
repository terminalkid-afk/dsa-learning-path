# Quick Sort

## 💡 Concept
Quick Sort is one of the most widely used sorting algorithms due to its incredible speed in practice. Like Merge Sort, it uses the **Divide and Conquer** strategy, but instead of splitting the list in the middle, it uses a **Pivot**.

The process works like this:
1. **Pick a Pivot**: Choose one element from the array as the "pivot".
2. **Partitioning**: Rearrange the array so that:
   - All elements **smaller** than the pivot are on its left.
   - All elements **larger** than the pivot are on its right.
3. **Recursion**: Now the pivot is in its final sorted position. Repeat the same process for the left and right subarrays.

**Imagine this:** You are organizing a line of people by height. You pick one person as a reference (the pivot). You tell everyone shorter than that person to move to the left and everyone taller to move to the right. Now, the pivot person is exactly where they should be. You then repeat this for the group on the left and the group on the right.

### Why do we need it?
- It is typically faster than Merge Sort in practice because it has better "cache locality" and requires no extra memory for temporary arrays.
- It is an **in-place** sorting algorithm.
- It is the default sorting algorithm used in many language libraries (like Java's `Arrays.sort()` for primitives).

## ⚙️ Visual Logic
**📺 See it in Action**: [Visualize Quick Sort here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

Suppose we have an array `[10, 80, 30, 90, 40, 50, 70]` and we pick the last element `70` as the pivot.

**Partitioning Step:**
1. Compare `10` with `70` $\rightarrow$ Smaller, stays left.
2. Compare `80` with `70` $\rightarrow$ Larger, stays right.
3. Compare `30` with `70` $\rightarrow$ Smaller, move to left.
4. Compare `90` with `70` $\rightarrow$ Larger, stays right.
5. Compare `40` with `70` $\rightarrow$ Smaller, move to left.
6. Compare `50` with `70` $\rightarrow$ Smaller, move to left.

**Result after first partition:** `[10, 30, 40, 50, 70, 90, 80]`
The pivot `70` is now in its **final correct position**. We now repeat the process for `[10, 30, 40, 50]` and `[90, 80]`.

## ⏱️ Complexity Analysis

| Case | Time Complexity | Why? |
| :--- | :--- | :--- |
| **Best Case** | $O(n \log n)$ | Pivot always splits the array into two equal halves. |
| **Average Case** | $O(n \log n)$ | Standard expected behavior. |
| **Worst Case** | $O(n^2)$ | Pivot is always the smallest or largest element (e.g., already sorted array). |

**Space Complexity:** $O(\log n)$ due to the recursive call stack.

## 💻 Implementation

Check out the [quick_sort.py](./quick_sort.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Sort an Array](https://leetcode.com/problems/sort-an-array/)
- [GeeksforGeeks: Quick Sort](https://www.geeksforgeeks.org/quick-sort/)
