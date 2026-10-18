# Insertion Sort

## 💡 Concept
Insertion Sort works similarly to the way you sort playing cards in your hands. You pick one card at a time and "insert" it into its correct position relative to the cards you've already sorted.

The array is virtually split into a **sorted part** and an **unsorted part**. Elements from the unsorted part are picked and placed at the correct position in the sorted part.

**Imagine this:** You are sorting a hand of cards. You hold the first card (it's sorted by default). You pick the second card; if it's smaller than the first, you slide it to the left. You pick the third card and slide it left until it hits a card smaller than itself.

### Why do we need it?
- It is very efficient for **small datasets**.
- It is **Adaptive**: If the array is already nearly sorted, it runs very fast ($O(n)$).
- It is **Stable**: Maintains the relative order of equal elements.

## ⚙️ Visual Logic
**📺 See it in Action**: [Visualize Insertion Sort here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

Suppose we have an array `[12, 11, 13, 5, 6]`.

1. **Step 1:** `[12]` is sorted. Pick `11`. `11 < 12`, so move `12` right and insert `11`. $\rightarrow$ `[11, 12, 13, 5, 6]`
2. **Step 2:** `[11, 12]` sorted. Pick `13`. `13 > 12`, so it stays. $\rightarrow$ `[11, 12, 13, 5, 6]`
3. **Step 3:** `[11, 12, 13]` sorted. Pick `5`. `5` is smaller than `13`, `12`, and `11`. Slide them all right and insert `5` at the start. $\rightarrow$ `[5, 11, 12, 13, 6]`
4. **Step 4:** `[5, 11, 12, 13]` sorted. Pick `6`. `6` is smaller than `13`, `12`, `11` but larger than `5`. Insert after `5`. $\rightarrow$ `[5, 6, 11, 12, 13]`

## ⏱️ Complexity Analysis

| Case | Time Complexity | Why? |
| :--- | :--- | :--- |
| **Best Case** | $O(n)$ | Array is already sorted; only one comparison per element. |
| **Worst Case** | $O(n^2)$ | Array is reverse sorted; must slide every element. |
| **Average Case** | $O(n^2)$ | Standard nested loop behavior. |

**Space Complexity:** $O(1)$ as it sorts in-place.

## 💻 Implementation

Check out the [insertion_sort.py](./insertion_sort.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Sort an Array](https://leetcode.com/problems/sort-an-array/)
- [GeeksforGeeks: Insertion Sort](https://www.geeksforgeeks.org/insertion-sort/)
