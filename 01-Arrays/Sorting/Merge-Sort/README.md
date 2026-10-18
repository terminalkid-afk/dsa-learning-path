# Merge Sort

## 💡 Concept
Merge Sort is a highly efficient, stable, and comparison-based sorting algorithm. It uses the **Divide and Conquer** strategy to sort a list.

The process is broken down into two main phases:
1. **Divide**: The list is recursively split into two halves until each sub-list contains only one element (a list with one element is naturally sorted).
2. **Conquer (Merge)**: The sorted sub-lists are merged back together in a way that maintains the sorted order until the entire list is reconstructed.

**Imagine this:** You have a giant pile of mixed-up papers. Instead of sorting them all at once, you split the pile in half, give one half to a friend, and keep the other. You both keep splitting your piles until you each have just one paper. Then, you start merging them back: you take two single papers, put the smaller one first, and now you have a sorted pair. You repeat this merging process until you have one perfectly sorted giant pile.

### Why do we need it?
- It provides a **guaranteed** time complexity of $O(n \log n)$, regardless of whether the input is sorted or not.
- It is used for sorting large datasets that don't fit in RAM (External Sorting).
- It is stable, meaning equal elements keep their original relative order.

## ⚙️ Visual Logic
**📺 See it in Action**: [Visualize Merge Sort here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

Suppose we have an array `[38, 27, 43, 3, 9, 82, 10]`.

**Divide Phase:**
`[38, 27, 43, 3, 9, 82, 10]` $\rightarrow$ `[38, 27, 43]` and `[3, 9, 82, 10]`
$\rightarrow$ `[38]` `[27, 43]` and `[3, 9]` `[82, 10]`
$\rightarrow$ `[38]` `[27]` `[43]` and `[3]` `[9]` `[82]` `[10]` (All single elements)

**Merge Phase:**
1. Merge `[27]` and `[43]` $\rightarrow$ `[27, 43]`
2. Merge `[38]` and `[27, 43]` $\rightarrow$ `[27, 38, 43]`
3. Merge `[3]` and `[9]` $\rightarrow$ `[3, 9]`
4. Merge `[82]` and `[10]` $\rightarrow$ `[10, 82]`
5. Merge `[3, 9]` and `[10, 82]` $\rightarrow$ `[3, 9, 10, 82]`
6. Final Merge: `[27, 38, 43]` and `[3, 9, 10, 82]` $\rightarrow$ `[3, 9, 10, 27, 38, 43, 82]`

## ⏱️ Complexity Analysis

| Case | Time Complexity | Why? |
| :--- | :--- | :--- |
| **Best Case** | $O(n \log n)$ | Always divides the list in half and merges. |
| **Worst Case** | $O(n \log n)$ | Always divides the list in half and merges. |
| **Average Case** | $O(n \log n)$ | Consistent performance. |

**Space Complexity:** $O(n)$ because we need temporary arrays to store the merged results.

## 💻 Implementation

Check out the [merge_sort.py](./merge_sort.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Sort an Array](https://leetcode.com/problems/sort-an-array/)
- [GeeksforGeeks: Merge Sort](https://www.geeksforgeeks.org/merge-sort/)
