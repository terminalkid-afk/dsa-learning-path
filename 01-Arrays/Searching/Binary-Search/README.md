# Binary Search

## 💡 Concept
Binary Search is a significantly faster searching algorithm than Linear Search, but it comes with one strict requirement: **the list must be sorted**. 

Instead of checking every element, Binary Search uses a "divide and conquer" strategy. It looks at the middle element of the list:
- If the middle element is the target, you're done!
- If the target is **smaller** than the middle, you ignore the entire right half.
- If the target is **larger** than the middle, you ignore the entire left half.

You repeat this process, cutting the search area in half every single time, until the target is found or the search area is empty.

**Imagine this:** You are looking for a word in a physical dictionary. You don't start at page 1; you open it in the middle. If the word you want comes after the current page, you ignore the first half of the book and repeat the process with the second half.

### Why do we need it?
- It is incredibly fast for large datasets.
- It reduces the search time from linear to logarithmic.

## ⚙️ Visual Logic
**📺 See it in Action**: [Visualize Binary Search here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

Suppose we have a sorted array `[10, 20, 30, 40, 50, 60, 70]` and we are looking for `60`.

1. **Step 1:** Midpoint is `40`. Is `60 == 40`? ❌ No. Is `60 > 40`? ✅ Yes. **Discard left half** `[10, 20, 30, 40]`.
2. **Step 2:** New search area is `[50, 60, 70]`. Midpoint is `60`. Is `60 == 60`? ✅ Yes! **Return index 5**.

## ⏱️ Complexity Analysis

| Case | Time Complexity | Why? |
| :--- | :--- | :--- |
| **Best Case** | $O(1)$ | Target is exactly at the first midpoint. |
| **Worst Case** | $O(\log n)$ | The search area is halved until only one element remains. |
| **Average Case** | $O(\log n)$ | Logarithmic growth is extremely slow (very efficient). |

**Space Complexity:** $O(1)$ for iterative implementation as we only use a few variables for indices.

## 💻 Implementation

Check out the [binary_search.py](./binary_search.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Binary Search](https://leetcode.com/problems/binary-search/)
- [GeeksforGeeks: Binary Search](https://www.geeksforgeeks.org/binary-search/)
