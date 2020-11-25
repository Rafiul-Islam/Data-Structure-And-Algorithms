class Node:
    def __init__(self, data):
        self.data = data
        self.level_order = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert_data(self, data, current_node):
        if current_node is None:
            self.root = Node(data)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self.insert_data(data, current_node.right)
        else:
            if current_node.level_order is None:
                current_node.level_order = Node(data)
            else:
                self.insert_data(data, current_node.level_order)

    def level_order(self, current_node):
        if current_node is None:
            return
        q.en_q(current_node)
        while not q.queue_empty():
            res = q.q_first()
            print(res.data, end=" ")
            if res.level_order is not None:
                q.en_q(res.level_order)
            if res.right is not None:
                q.en_q(res.right)
            q.d_q()


class QNode:
    def __init__(self, node):
        self.node = node
        self.next = None


class Queue:
    def __init__(self):
        self.next = None
        self.prev = None

    def en_q(self, node):
        newNode = QNode(node)
        if self.prev is None:
            self.next = newNode
            self.prev = newNode
        else:
            self.prev.next = newNode
            self.prev = self.prev.next

    def d_q(self):
        if self.next is None:
            return
        self.next = self.next.next
        if self.next is None:
            self.prev = None

    def queue_empty(self):
        if self.next is None:
            return True
        return False

    def q_first(self):
        return self.next.node


q = Queue()
bst = BST()

bst.insert_data(15, bst.root)
bst.insert_data(10, bst.root)
bst.insert_data(20, bst.root)
bst.insert_data(25, bst.root)
bst.insert_data(8, bst.root)
bst.insert_data(12, bst.root)

bst.level_order(bst.root)
