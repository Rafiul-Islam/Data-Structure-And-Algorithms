class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current = self.head

        while current.next != None:
            current = current.next
        current.next = new_node

    def length(self):
        current_node = self.head
        total = 0
        while current_node.next != None:
            total += 1
            current_node = current_node.next

        print("Length:", total)
        return total

    def show(self):
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            print(current_node.data, end=" ")
        print()

    def get(self, index):
        if index > self.length():
            print('Error: Index out of bound')
            return
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:
                print(f"Value at {index}th position: {current_node.data}")
                return
            else:
                current_index += 1

    def remove(self, index):
        if index > self.length():
            print('Error: Index out of bound')
            return
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1


linkedList = LinkedList()
linkedList.append(5)
linkedList.append(2)
linkedList.append(3)
linkedList.append(4)
linkedList.show()
linkedList.length()
linkedList.get(2)
linkedList.remove(2)
linkedList.show()
