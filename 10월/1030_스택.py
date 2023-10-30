size = 5
list = [None] * size
top = -1

def isEmpty():
    return top == -1

def isFull():
    return top == size - 1

def push(e):
    global top
    if not isFull():
        top = top + 1
        list[top] = e
        print(list)
    else:
        print("stack overflow")

def pop():
    global top
    if not isEmpty():
        print("pop:" + str(list[top]))
        list[top] = None
        top = top - 1
        print(list)
    else:
        print("stack underflow")

def peek():
    global top
    if not isEmpty():
        print("peek:" + str(list[top]))
        print(list)
    else:
        print("stack underflow")

push(1)
push(2)
push(3)
push(4)
push(5)
push(6)
pop()
pop()
pop()
pop()
pop()
pop()