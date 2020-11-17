class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def create_node(data):
    new_node = Node(data)
    if new_node is None:
        print('Could not create a new node')
        return
    return new_node


def add_left_child(node, left_child):
    node.left = left_child


def add_right_child(node, right_child):
    node.right = right_child


def create_tree():
    root = create_node(2)
    left1 = create_node(7)
    right1 = create_node(9)
    add_left_child(root, left1)
    add_right_child(root, right1)
    left2 = create_node(1)
    right2 = create_node(6)
    add_left_child(left1, left2)
    add_right_child(left1, right2)
    left3 = create_node(5)
    right3 = create_node(10)
    add_left_child(right2, left3)
    add_right_child(right2, right3)
    right1_right1 = create_node(8)
    add_right_child(right1, right1_right1)
    right1_left2 = create_node(3)
    right1_right2 = create_node(4)
    add_left_child(right1_right1, right1_left2)
    add_right_child(right1_right1, right1_right2)

    return root


def inorder(root):
    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.data) + "->", end='')
        # Traverse right
        inorder(root.right)


def postorder(root):
    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.data) + "->", end='')


def preorder(root):
    if root:
        # Traverse root
        print(str(root.data) + "->", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)


tree_root = create_tree()

print("Inorder traversal ")
inorder(tree_root)

print("\nPreorder traversal ")
preorder(tree_root)

print("\nPostorder traversal ")
postorder(tree_root)
