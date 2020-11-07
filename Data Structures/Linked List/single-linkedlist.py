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

    def append_first(self, data):
        new_node = Node(data)
        current_node = self.head
        start = current_node.next
        new_node.next = start
        start = new_node
        current_node.next = start
        while current_node.next != None:
            current_node = current_node.next

    def append_nth_position(self, index, data):
        new_node = Node(data)
        current_node = self.head
        current_index = 0
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = new_node
                new_node.next = current_node
                return
            else:
                current_index += 1

    def length(self):
        current_node = self.head
        total = 0
        while current_node.next != None:
            total += 1
            current_node = current_node.next

        # print(F"Length: {total}" if total > 0 else "Empty LinkedList")
        return total

    def is_empty(self):
        if self.length() == 0:
            print('Empty LinkedList')
            return
        else:
            print("Not empty")
            return

    def show(self):
        if self.length() == 0:
            self.is_empty()
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            print(current_node.data, end=" ")
        print()

    def get(self, index):
        if self.length() == 0:
            self.is_empty()

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

    def remove(self, index=0):
        if self.length() == 0:
            self.is_empty()
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
linkedList.is_empty()
linkedList.show()
linkedList.remove()
linkedList.show()
# linkedList.remove(0)
# linkedList.append(2)
# linkedList.append(3)
# linkedList.append(4)
# linkedList.show()
# linkedList.length()
# linkedList.append_first(1)
# linkedList.show()
# linkedList.length()
# linkedList.append_nth_position(2, 6)
# linkedList.length()
# linkedList.show()
# linkedList.get(2)
# linkedList.remove(2)
# linkedList.show()
# linkedList.remove(2)
# linkedList.show()
# linkedList.remove(2)
# linkedList.show()
# linkedList.remove(2)
# linkedList.show()
