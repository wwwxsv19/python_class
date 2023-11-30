class Stack:
    def __init__(self, size):
        self.size = size
        self.list = [None] * self.size
        self.top = -1
    
    def isFull(self):
        return self.top == self.size - 1
    
    def isEmpty(self):
        return self.top == -1
    
    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.list[self.top] = item
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
            return self.list[self.top]
        else:
            print("Stack is underflow!")

    def printStack(self):
        print(self.list)
    
s = Stack(10)
expr = input()
output = ''

for c in expr:
    if c in '+-':
        while not s.isEmpty() and s.peek() in '*/+-':
            output += s.pop()
        s.push(c)
    elif c in '*/(':
        s.push(c)
    elif c == ')':
        while not s.isEmpty() and s.peek() != '(': 
            output += s.pop()
        if not s.isEmpty() and s.peek() == '(':
            s.pop()
    else:
        output += c
    
while not s.isEmpty():
    output += s.pop()

print(output)