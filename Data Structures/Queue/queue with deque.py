from collections import deque


class Queue:
    def __init__(self):
        self.container = deque([])

    def push(self, data):
        self.container.insert(0, data)

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
        print("Empty Queue" if len(self.container) == 0 else "Not Empty Queue")

    def size(self):
        print("Queue Size:", len(self.container))

    def print(self):
        if len(self.container) == 0:
            self.is_empty()
            return
        print("Queue:", *self.container)


Queue = Queue()
Queue.push(5)
Queue.push(2)
Queue.push(1)
Queue.print()
Queue.peek()
print("Pop:", Queue.pop())
Queue.print()
Queue.peek()
Queue.size()
print("Pop:", Queue.pop())
Queue.size()
Queue.is_empty()
print("Pop:", Queue.pop())
Queue.size()
Queue.is_empty()
