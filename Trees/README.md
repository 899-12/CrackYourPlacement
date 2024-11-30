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
