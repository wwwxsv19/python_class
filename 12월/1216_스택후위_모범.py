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

def pre(c): # 연산자 간의 우선순위를 결정하는 함수
    if c == '(' or c == ')': 
        return 0
    elif c == '+' or c == '-':
        return 1
    elif c == '*' or c=='/':
        return 2
    else:
        return -1

def POPIPOPI(expr):
    s = Stack(10)
    output = ''

    for c in expr:
        if c in '(':
            s.push(c)
        elif c in ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output += op
        elif c in '+-*/':
            while not s.isEmpty():
                op = s.peek()
                if pre(c) <= pre(op):
                    output += op
                    s.pop()
                else:
                    break
            s.push(c)
        else:
            output += c
        
    while not s.isEmpty():
        output += s.pop()

    return output


expr = input()
print(POPIPOPI(expr))