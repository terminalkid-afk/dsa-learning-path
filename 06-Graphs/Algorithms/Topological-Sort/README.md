# Topological Sort

## 💡 Concept
**Topological Sorting** for a Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge $u \rightarrow v$, vertex $u$ comes before $v$ in the ordering.

In simpler terms, it is used to determine the correct sequence of tasks when some tasks depend on others.

**Imagine this:** Getting dressed.
- You must put on your **Socks** before your **Shoes**.
- You must put on your **Shirt** before your **Jacket**.
- You must put on your **Underwear** before your **Pants**.
The sequence `Underwear -> Pants -> Socks -> Shoes -> Shirt -> Jacket` is a topological sort of your dressing process. If you tried to put your shoes on first, you'd be doing it in the wrong order!

### Key Requirements
1. **Directed**: The edges must have a direction (dependencies).
2. **Acyclic**: The graph must have **no cycles**. If there is a cycle (e.g., A depends on B, B depends on C, and C depends on A), a topological sort is impossible because no one can start first.

## ⚙️ Algorithms for Topological Sort
There are two main ways to implement this:
1. **Kahn's Algorithm (BFS-based)**: 
   - Find all nodes with **in-degree 0** (no dependencies).
   - Add them to a queue and "remove" them from the graph, decreasing the in-degree of their neighbors.
   - Repeat until all nodes are processed.
2. **DFS-based Algorithm**:
   - Perform a standard DFS.
   - Once a node's children are all visited (the recursive call returns), push the node onto a stack.
   - The reverse of the stack is the topological sort.

## ⏱️ Complexity Analysis
**📺 See it in Action**: [Visualize Topological Sort here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

| Aspect | Complexity | Why? |
| :--- | :--- | :--- |
| **Time Complexity** | $O(V + E)$ | Every vertex and edge is visited once. |
| **Space Complexity** | $O(V)$ | To store the in-degrees or the recursion stack. |

## 💻 Implementation

Check out the [topological_sort.py](./topological_sort.py) file for the clean Python implementation using Kahn's Algorithm.

## 🚀 Practice Problems
- [LeetCode: Course Schedule](https://leetcode.com/problems/course-schedule/) (The classic Topological Sort problem!)
- [LeetCode: Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
- [GeeksforGeeks: Topological Sorting](https://www.geeksforgeeks.org/topological-sorting/)
