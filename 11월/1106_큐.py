class CircleQueue:
    def __init__(self, size = 5):
        self.size = size
        self.list = [None] * size
        self.front = 0
        self.rear = 0

q = CircleQueue()

def isEmpty():
    return q.rear == q.front

def isFull():
	return (q.rear + 1) % q.size == q.front

def enQueue(e):
    if not isFull():
        q.rear = (q.rear + 1) % q.size
        q.list[q.rear] = e
        print(q.list)
    else:
        print("stack overflow")

def deQueue():
    if not isEmpty():
        q.front = (q.front + 1) % q.size
        q.list[q.front] = None
        print(q.list)
    else:
        print("stack underflow")

enQueue(1)
enQueue(2)
enQueue(3)
enQueue(4)
enQueue(5)
deQueue()
deQueue()
deQueue()
enQueue(1)
enQueue(2)
enQueue(3)