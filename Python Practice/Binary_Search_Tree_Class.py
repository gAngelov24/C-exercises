# 5. Binary Search Tree Class : w3resource
# Write a Python program to create a class representing a binary search tree. 
# Include methods for inserting and searching for elements in the binary tree.
class Node:
    def __init__(self, node_data):
        self.data = node_data
        self.left = None
        self.right = None
        
class BST:
    #           6
    #         /   \
    #       4       7
    #     /   \       \
    #    3     5        9
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None
    def insert(self, node_data):
      node = Node(node_data)
        
      if not self.root:
        self.root = node
      else:
        success = self.helper(self.root, node)
        if success != 1:
          print("ERROR: insert node failed!")

    def helper(self, root, node):
      if node.data < root.data:
        if root.left is None:             
          root.left = node
          return 1
        else:
          return self.helper(root.left, node)
      else:
        if root.right is None:             
          root.right = node
          return 1
        else:
          return self.helper(root.right, node)
    def find(self, num):
        start = self.root
        while start is not None:
            if start.data < num:
                start = start.right
            elif start.data > num:
                start = start.left
            else:
                return start
        return None

bst = BST()

# Insert values into the BST
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

# Search for elements in the BST and print the results
print("Searching for elements:")
print(bst.find(4))  # Found, returns the node (4)
print(bst.find(9))  # Not found, returns None 