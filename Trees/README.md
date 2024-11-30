# 1.Binary Tree Height Calculation

This project demonstrates how to calculate the height of a binary tree in Python using recursion. The implementation includes a `Node` class to represent the tree nodes and a static method to compute the height of the tree.

## Definition of Tree Height

The height of a binary tree is defined as the number of edges on the longest path from the root node to a leaf node:

- For a single-node tree, the height is `1`.
- For an empty tree, the height is `0`.

## Features

- Calculate the height of a binary tree using a recursive function.
- Implements basic operations on binary trees to construct and traverse nodes.
- Demonstrates the use of static methods in Python for utility functions.

## Project Structure

### Classes

1. **`Node`**:
   - Represents a node in the binary tree.
   - **Attributes**:
     - `data`: Stores the value of the node.
     - `left`: A reference to the left child of the node.
     - `right`: A reference to the right child of the node.
   - **Method**:
     - `height`: A static method to calculate the height of the binary tree.

## Code Example

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

   
    def height(root):
        if root is None:
            return 0
        left_height = Node.height(root.left)
        right_height = Node.height(root.right)
        return max(left_height, right_height) + 1

if __name__ == "__main__":
    # Create a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Calculate the height of the tree
    print("Height of the tree:", Node.height(root))

```
# 2.Binary Tree Size Calculation
This Python program defines a binary tree structure using the Node class and calculates the size of the binary tree, which is the total number of nodes in the tree. The size is determined using a recursive approach.

Problem Overview
Given a binary tree, the size of the tree is defined as the number of nodes present in the tree. A node is counted if it is not None, and the total size is the sum of the nodes in the left subtree, right subtree, and the current node.

### Binary Tree Representation:
A binary tree is made up of nodes, where each node has:

**Data:** Stores the value or information.
**Left Child:** Points to the left child node.
**Right Child:** Points to the right child node.
In this code, a binary tree is constructed and its size is calculated by traversing the tree.

### Code Explanation
Node Class
The Node class defines the structure of a binary tree node:

__init__(self, data): Initializes the node with a given value (data), and sets the left and right children to None.
size(root): A static method that calculates the size of the binary tree starting from the root node. The method works recursively:
If the node is None, return 0.
Recursively calculate the size of the left and right subtrees.
The total size is the size of the left subtree + the size of the right subtree + 1 (for the current node).

#### Complexity Analysis
### Time Complexity:
The function size(root) traverses each node in the tree exactly once.
For each node, the size of the left and right subtrees is calculated recursively.
Thus, the time complexity of this code is O(n), where n is the number of nodes in the tree.
### Space Complexity:
The space complexity is O(h), where h is the height of the tree, due to the recursive call stack. In the worst case, the height of the tree is O(n) (for a skewed tree), but in the best case (a balanced tree), the height is O(log n).