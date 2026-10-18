# Introduction to Linked Lists

## 💡 Concept
A **Linked List** is a linear data structure where elements are not stored at contiguous memory locations. Instead, each element is a separate object called a **Node**.

Each **Node** consists of two parts:
1. **Data**: The actual value you want to store.
2. **Next (Pointer/Reference)**: A link to the next node in the sequence.

The list starts with a pointer to the first node, called the **Head**. The last node in the list points to `None` (or `Null`), indicating the end of the list.

**Imagine this:** A scavenger hunt. 
- You start at the first clue (the **Head**).
- The first clue tells you where to find the second clue.
- The second clue tells you where to find the third, and so on.
- The final clue says "The end," and there are no more clues to follow.

### Why do we need Linked Lists?
Unlike Arrays, Linked Lists offer several advantages:
- **Dynamic Size**: They can grow or shrink during runtime without needing to reallocate the entire structure.
- **Efficient Insertions/Deletions**: Adding or removing an element doesn't require shifting all other elements (unlike arrays). You simply change a few pointers.

### Linked List vs. Array: A Quick Comparison

| Feature | Array | Linked List |
| :--- | :--- | :--- |
| **Memory** | Contiguous (Side-by-side) | Non-contiguous (Scattered) |
| **Size** | Fixed (mostly) | Dynamic |
| **Access** | $O(1)$ (Index-based) | $O(n)$ (Sequential) |
| **Insert/Delete** | $O(n)$ (due to shifting) | $O(1)$ (if pointer is known) |

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Why? |
| :--- | :--- | :--- |
| **Access/Search** | $O(n)$ | Must start from the Head and traverse. |
| **Insert (at Head)** | $O(1)$ | Just update the Head pointer. |
| **Delete (at Head)** | $O(1)$ | Just move the Head pointer. |
| **Insert (at End)** | $O(n)$ | Must traverse to the end first. |

---

## 🚀 Learning Path for Linked Lists
In this section, we will cover:
1. **Types**: Singly, Doubly, and Circular Linked Lists.
2. **Operations**:
   - **Traversal**: Visiting every node.
   - **Insertion**: Adding nodes at the start, end, or middle.
   - **Deletion**: Removing nodes from various positions.
   - **Searching**: Finding a specific value.
   - **Advanced**: Reversing, merging, and comparing lists.
