class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert_data(self, data, current_node):
        if self.root is None:
            new_node = Node(data)
            self.root = new_node
            return
        else:
            if current_node is None:
                current_node = Node(data)
            elif data > current_node.data:
                current_node.right = self.insert_data(data, current_node.right)
            else:
                current_node.left = self.insert_data(data, current_node.left)
            return current_node

    def search_data(self, data, current_node):
        if current_node is None:
            return False
        elif data == current_node.data:
            return True
        elif data > current_node.data:
            return self.search_data(data, current_node.right)
        else:
            return self.search_data(data, current_node.left)

    def find_min_value(self, current_node):
        min_value = current_node.data
        while current_node is not None:
            min_value = current_node.data
            current_node = current_node.left
        return min_value

    def delete_data(self, data, current_node):
        if current_node is None:
            return current_node
        elif current_node.data > data:
            current_node.left = self.delete_data(data, current_node.left)
        elif current_node.data < data:
            current_node.right = self.delete_data(data, current_node.right)
        else:
            if current_node.left is None and current_node.right is None:
                current_node = None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                current_node.data = self.find_min_value(current_node.right)
                current_node.right = self.delete_data(current_node.data, current_node.right)
        return current_node

    def in_order_traversal(self, current_node):
        if current_node is None:
            return
        self.in_order_traversal(current_node.left)
        print(current_node.data, end=' ')
        self.in_order_traversal(current_node.right)


bst = BST()
bst.insert_data(15, bst.root)
bst.insert_data(10, bst.root)
bst.insert_data(20, bst.root)
bst.insert_data(25, bst.root)
bst.insert_data(8, bst.root)
bst.insert_data(12, bst.root)
bst.insert_data(11, bst.root)
bst.insert_data(9, bst.root)
bst.insert_data(2, bst.root)

bst.in_order_traversal(bst.root)
print()
# print('Exist' if bst.search_data(8, bst.root) else 'Not Exist')
# print('Exist' if bst.search_data(14, bst.root) else 'Not Exist')
# print('Min Value:', bst.find_min_value(bst.root))

bst.delete_data(10, bst.root)
bst.in_order_traversal(bst.root)

print()
bst.delete_data(20, bst.root)
bst.in_order_traversal(bst.root)
