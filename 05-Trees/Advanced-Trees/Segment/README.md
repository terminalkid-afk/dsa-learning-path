# Segment Tree

## 💡 Concept
A **Segment Tree** is a specialized tree used for storing information about intervals or segments. It allows querying which of the stored segments contain a given point, or querying the aggregate (sum, min, max) of a range in an array.

While a simple array allows $O(1)$ updates but $O(n)$ range queries, and a prefix sum array allows $O(1)$ range queries but $O(n)$ updates, a Segment Tree provides a perfect balance: **both updates and range queries take $O(\log n)$**.

**Imagine this:** You are managing a large warehouse of 1,000 boxes. You want to know the total weight of boxes from index 200 to 500. Instead of adding 300 boxes every time, you have a "summary" system. You have one box that knows the total weight of 1-1,000, two boxes for 1-500 and 501-1,000, and so on. To find the weight of 200-500, you only need to look at a few "summary" boxes.

### Why do we need Segment Trees?
- **Range Queries**: Efficiently finding the sum, minimum, or maximum in a sub-range of an array.
- **Point Updates**: Quickly updating a single element in the array without recalculating everything.
- **Competitive Programming**: Essential for problems involving dynamic range updates and queries.

## ⏱️ Complexity Analysis
**📺 See it in Action**: [Visualize Segment Trees here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

| Operation | Time Complexity | Why? |
| :--- | :--- | :--- |
| **Build Tree** | $O(n)$ | We create $2n-1$ nodes. |
| **Range Query** | $O(\log n)$ | We only visit at most 4 nodes per level of the tree. |
|, **Point Update**| $O(\log n)$ | We only update nodes along the path to the root. |

**Space Complexity:** $O(n)$ (typically $4n$ nodes are allocated for safety).

## 💻 Implementation

Check out the [segment_tree.py](./segment_tree.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/)
- [GeeksforGeeks: Segment Tree](https://www.geeksforgeeks.org/segment-tree/)
