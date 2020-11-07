class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkeList:
    def __init__(self):
        self.top = Node()

    def Enqueue(self, data):
        new_node = Node(data)
        current = self.top
        while current.next != None:
            current = current.next
        current.next = new_node
