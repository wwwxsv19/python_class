class Stack:
    def __init__(self, size = 5):
        self.size = size
        self.list = [None] * size
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.size - 1

    def push(self, e):
        if not self.isFull():
            self.top = self.top + 1
            self.list[self.top] = e
            print(self.list)
        else:
            print("stack overflow")

    def pop(self):
        if not self.isEmpty():
            print(self.list[self.top], end=" ")
            self.list[self.top] = None
            self.top = self.top - 1
            print(self.list)
        else:
            print("stack underflow")

    def peek(self):
        if not self.isEmpty():
            print(self.list[self.top])
        else:
            print("stack is underflow")

s = Stack()

s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()