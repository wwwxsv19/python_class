class Stack:
    def __init__(self, size):
        self.size = size
        self.list = [None] * size
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.size - 1

    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.list[self.top] = item
            print(self.list)
        else:
            print("Stack is overflow!")

    def pop(self):
        if not self.isEmpty():
            temp = self.list[self.top]
            self.list[self.top] = None
            self.top -= 1
            return temp
        else:
            print("Stack is underflow!")

    def peek(self):
        if not self.isEmpty():
            return(self.list[self.top])
        else:
            print("Stack is underflow!")