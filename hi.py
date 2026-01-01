class Stack:
    def _init_(self):
        self.stack = []
        self.size = 0

    def push(self, item):
        self.stack.append(item)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("Pop from an empty stack")
        self.size -= 1
        return self.stack.pop()

    def peek(self):
        if self.size == 0:
            raise IndexError("Peek from an empty stack")
        return self.stack[-1]

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size