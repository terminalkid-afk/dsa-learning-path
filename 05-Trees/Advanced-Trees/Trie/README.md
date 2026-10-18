# Trie (Prefix Tree)

## 💡 Concept
A **Trie** (pronounced "try") is a specialized tree used to store a dynamic set of strings. Unlike a binary tree, where nodes store values, in a Trie, the **path from the root to a node** represents the value.

Each node in a Trie typically contains:
1. A map or array of children (one for each possible character).
2. A boolean flag `isEndOfWord` to mark if a complete word ends at this node.

**Imagine this:** A dictionary's index. To find the word "APPLE", you first go to the 'A' section, then the 'P' section within 'A', then 'P' within that, and so on. Many words share the same prefix (e.g., "APPLE", "APPLY", "APRICOT" all start with "AP"). A Trie stores this shared prefix only once, saving space and making searches incredibly fast.

### Why do we need Tries?
- **Autocomplete/Auto-suggest**: When you type in a search bar, the system uses a Trie to find all words that start with your current prefix.
- **Spell Checkers**: Quickly verifying if a word exists in a dictionary.
- **IP Routing**: Longest prefix matching in network routers.

## ⏱️ Complexity Analysis
**📺 See it in Action**: [Visualize Tries here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

| Operation | Time Complexity | Why? |
| :--- | :--- | :--- |
| **Insert** | $O(L)$ | $L$ is the length of the word being inserted. |
| **Search** | $O(L)$ | We only traverse down the length of the word. |
| **Prefix Search**| $O(L)$ | Finding all words with a prefix takes $O(L)$. |

**Space Complexity:** $O(A \times N \times L)$ where $A$ is the alphabet size, $N$ is number of words, and $L$ is avg length.

## 💻 Implementation

Check out the [trie.py](./trie.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)
- [LeetCode: Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
