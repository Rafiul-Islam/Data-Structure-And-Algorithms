class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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


def print_in_pre_order(root, li):
    current_node = root
    if current_node.left is not None:
        li.append(current_node.left.data)
        print_in_pre_order(current_node.left, li)
    if current_node.right is not None:
        li.append(current_node.right.data)
        print_in_pre_order(current_node.right, li)


if __name__ == '__main__':
    tree_root = create_tree()
    result_pre_order = [tree_root.data]
    print_in_pre_order(tree_root, result_pre_order)
    print("PrOrder: ", *result_pre_order)
