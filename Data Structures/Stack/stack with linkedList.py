class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.top = None
        self.node_count = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.node_count += 1

    def pop(self):
        if self.top is None:
            self.isEmpty()
            return
        cur = self.top.data
        self.top = self.top.next
        self.node_count -= 1
        return f"Pop: {cur}"

    def peek(self):
        if self.top is None:
            self.isEmpty()
            return
        print('Peek:', self.top.data)

    def is_empty(self):
        if self.top is None:
            self.empty_stack()
            return
        print('Not Empty Stack')

    def empty_stack(self):
        print('Empty Stack')

    def size(self):
        if self.top is None:
            self.empty_stack()
            return
        print('Stack size:', self.node_count)

    def print(self):
        if self.top is None:
            self.empty_stack()
            return
        current = self.top

        print("Stack: ")
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print("\n----------")


stack = LinkedList()
stack.push(5)
stack.push(2)
stack.push(1)
stack.print()
print(stack.pop())
stack.print()
stack.peek()
stack.is_empty()
stack.size()
stack.print()
print(stack.pop())
print(stack.pop())
stack.size()
stack.print()
print(stack.pop())
