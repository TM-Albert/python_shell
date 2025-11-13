# FIND AND LEARN ABOUT THE TREE DATA STRUCTURE 

from collections import deque

data = [
    {
        "command": "echo",
        "args": ["Hello     world"],
        "stdin_redirect": "./cmd/files/mop.md",
        "stdout_redirect": None,
        "operator": "&&"
    },
    {   
        "command": "echo",
        "args": ["Hello", "world"],
        "stdin_redirect": False,
        "stdout_redirect": False,
        "operator": None
    }
]


root = [1,2,2,3,4,4,3]

class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right


class Solution:
    def __init__(self):
        root = [1,2,2,3,4,4,3]

        self.tree_root = TreeNode(root[0])

        self.tree_root.left = TreeNode(root[1])
        self.tree_root.right = TreeNode(root[2])

        left = self.tree_root.left
        right = self.tree_root.right

        left.left = TreeNode(root[3])
        left.right = TreeNode(root[4])
        right.left = TreeNode(root[5])
        right.right = TreeNode(root[6])

    def _with_root(func):
        def wrapper(self, node=None, level=0):
            if node is None and level == 0:
                node = self.tree_root

            elif node is None:
                return True
            
            return func(self, node, level)
        return wrapper
    

    # --- Tree traversals ---
    @_with_root
    def print_tree(self, node, level):
        self.print_tree(node.right, level + 1)
        print("         " * level + f"-> {node.data}")
        self.print_tree(node.left, level + 1)

    @_with_root
    def print_only_left(self, node, level):
        print("         " * level + f"-> {node.data}")
        self.print_only_left(node.left, level + 1)

    @_with_root
    def print_only_right(self, node, level):
        print("         " * level + f"-> {node.data}")
        self.print_only_right(node.right, level + 1)
        


Solution().print_tree()
Solution().print_only_left()
Solution().print_only_right()


# simple linked list
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def print_data(self):
        print(self.data)

node7 = Node(1781)
node6 = Node(891, node7)
node5 = Node(78, node6)
node4 = Node(62, node5)
node3 = Node(89, node4)
node2 = Node(76, node3)
node1 = Node(12, node2)

root = Node(1, node1)

def print_nodes(root_node):
    if root_node:
        root_node.print_data()
        print_nodes(root_node.next)

def add_node(root_node, data):
    if root_node.next:
        root_node.print_data()
        add_node(root_node.next, data)
    else:
        new_node = Node(data)
        root_node.next = new_node
        return
    
# print_nodes(root)
# add_node(root, 89218)
# print_nodes(root)

