# Trie Implementation in Python

"""
Goal: Implement a Trie (Prefix Tree) for efficient string storage and retrieval.
Algorithm: Use a nested dictionary to represent children and a flag for end-of-word.
"""

class TrieNode:
    def __init__(self):
        # Dictionary to store children: { character: TrieNode }
        self.children = {}
        # Flag to mark the end of a complete word
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        Time Complexity: O(L), where L is the length of the word.
        """
        node = self.root
        for char in word:
            # If the character is not present, create a new TrieNode
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the child node
            node = node.children[char]

        # Mark the last node as the end of a word
        node.is_end_of_word = True
        print(f"Inserted word: '{word}'")

    def search(self, word):
        """
        Returns True if the word is in the trie.
        Time Complexity: O(L)
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end_of_word

    def starts_with(self, prefix):
        """
        Returns True if there is any word in the trie that starts with the given prefix.
        Time Complexity: O(L)
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True

# --- Usage Example ---
if __name__ == "__main__":
    trie = Trie()

    # Insert some words
    words = ["apple", "apply", "app", "ball", "bat"]
    for w in words:
        trie.insert(w)

    # Test Case 1: Exact word search
    print(f"Search 'apple': {trie.search('apple')}")   # Expected: True
    print(f"Search 'app': {trie.search('app')}")       # Expected: True
    print(f"Search 'appl': {trie.search('appl')}")     # Expected: False (prefix only)

    # Test Case 2: Prefix search (Autocomplete logic)
    print(f"Starts with 'ap': {trie.starts_with('ap')}") # Expected: True
    print(f"Starts with 'ba': {trie.starts_with('ba')}") # Expected: True
    print(f"Starts with 'cat': {trie.starts_with('cat')}") # Expected: False
