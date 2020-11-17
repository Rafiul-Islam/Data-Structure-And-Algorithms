class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.data) + "->", end=' ')
        inorder(root.right)


def insert(node, data):
    if node is None:
        return Node(data)

    if data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)

    return node


def minValueNode(node):
    current = node

    # Find the leftmost leaf
    while (current.left is not None):
        current = current.left

    return current


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal: ", end=' ')
inorder(root)

