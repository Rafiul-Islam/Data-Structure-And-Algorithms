from collections import deque


class Stack:
    def __init__(self):
        self.container = deque([])

    def push(self, data):
        self.container.append(data)

    def pop(self):
        if len(self.container) == 0:
            self.is_empty()
            return
        return self.container.pop()

    def peek(self):
        if len(self.container) == 0:
            self.is_empty()
            return
        print("Peek:", self.container[-1])

    def is_empty(self):
        print("Empty Stack" if len(self.container) == 0 else "Not Empty Stack")

    def size(self):
        print("Stack Size:", len(self.container))

    def print(self):
        if len(self.container) == 0:
            self.is_empty()
            return
        print("Stack:", *self.container)


stack = Stack()
stack.push(5)
stack.push(2)
stack.push(1)
stack.print()
stack.peek()
print("Pop:", stack.pop())
stack.peek()
stack.size()
print("Pop:", stack.pop())
stack.size()
stack.is_empty()
print("Pop:", stack.pop())
stack.size()
stack.is_empty()
