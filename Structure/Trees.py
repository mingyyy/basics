# complete tree (totally filled other than the rightmost elements on the last level) + full tree (none of the node has one child) = perfect tree
# Binary heaps: min heap() & max heap()


class TreeNode:
    # A complete binary tree where each node is smaller than it's children.
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def preorder_tree(root):
    if root.val is not None:
        print(root.val)
    if root.left is not None:
        preorder_tree(root.left)
    if root.right is not None:
        preorder_tree(root.right)


def inorder_tree(root):
    if root.left is not None:
        inorder_tree(root.left)
    if root.val is not None:
        print(root.val)
    if root.right is not None:
        inorder_tree(root.right)


def postorder_tree(root):
    if root.left is not None:
        postorder_tree(root.left)
    if root.right is not None:
        postorder_tree(root.right)
    if root.val is not None:
        print(root.val)

# construct a tree
'''
     1
   2   3
 4  5 6  7
'''
root = TreeNode(1, TreeNode(2), TreeNode(3))
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, TreeNode(6), TreeNode(7))


print(root, root.left, root.right, root.left.left, root.left.right, root.right.left, root.right.right)
print('preorder')
preorder_tree(root)
print('inorder')
inorder_tree(root)
print('postorder')
postorder_tree(root)

class MinHeap:
    def insert(self):
        # start from right most bottom
        pass
    def extract_min(self):
        pass
