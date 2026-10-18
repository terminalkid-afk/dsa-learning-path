# Linear Search

## 💡 Concept
Linear Search is the simplest searching algorithm. It starts from the beginning of a list and checks every single element one by one until it finds the target value or reaches the end of the list.

**Imagine this:** You are looking for a specific page in a book, and you flip through every single page from page 1 until you find it. That's Linear Search!

### Why do we need it?
- It works on **unsorted** data.
- It is extremely easy to implement.
- It is efficient for very small lists.

## ⚙️ Visual Logic
**📺 See it in Action**: [Visualize Linear Search here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

Suppose we have an array `[10, 20, 30, 40, 50]` and we are looking for `30`.

1. **Step 1:** Check index 0. Is `10 == 30`? ❌ No. Move to next.
2. **Step 2:** Check index 1. Is `20 == 30`? ❌ No. Move to next.
3. **Step 3:** Check index 2. Is `30 == 30`? ✅ Yes! **Return index 2**.

If we reached the end without finding the target, we would return `-1`.

## ⏱️ Complexity Analysis

| Case | Time Complexity | Why? |
| :--- | :--- | :--- |
| **Best Case** | $O(1)$ | Target is the first element. |
| **Worst Case** | $O(n)$ | Target is the last element or not present. |
| **Average Case** | $O(n)$ | On average, we search half the list. |

**Space Complexity:** $O(1)$ as we don't use any extra memory that scales with the input size.

## 💻 Implementation

Check out the [linear_search.py](./linear_search.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Find Target Indices After Sorting Array](https://leetcode.com/problems/find-target-indices-after-sorting-array/)
- [GeeksforGeeks: Linear Search](https://www.geeksforgeeks.org/linear-search/)
