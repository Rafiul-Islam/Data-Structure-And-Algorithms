INITIAL_CAPACITY = 50


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"({self.key}: {self.value}, Next: {self.next})"


class HashTable:
    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.bucket_list = [None] * self.capacity

    def hash(self, key):
        hash_sum = 0
        for index, value in enumerate(key):
            hash_sum += (index + len(key)) ** ord(value)
            hash_sum = hash_sum % self.capacity
        return hash_sum

    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.bucket_list[index]
        if node is None:
            self.bucket_list[index] = Node(key, value)
            return
        else:
            prev = node
            while node is not None:
                prev = node
                node = node.next
            prev.next = Node(key, value)

    def find(self, key):
        index = self.hash(key)
        node = self.bucket_list[index]

        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def remove(self, key):
        index = self.hash(key)
        node = self.bucket_list[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                self.bucket_list[index] = node.next
            else:
                prev.next = prev.next.next
            return result

    def print_hast_table(self):
        for ele in self.bucket_list:
            if ele:
                print(ele, end=" ")
        print()


hast_table = HashTable()
hast_table.insert('one', 101)
hast_table.insert('two', 102)
hast_table.insert('three', 103)
hast_table.insert('one', 105)
hast_table.print_hast_table()
print(hast_table.find('one'))
hast_table.remove('one')
hast_table.print_hast_table()
