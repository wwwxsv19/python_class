class circleQueue:
    def __init__(self, size):
        self.size = size
        self.list = [None] * self.size
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.rear == self.front

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def enQueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.size
            self.list[self.rear] = item
        else:
            print("Queue is overflow!")

    def deQueue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.size
            temp = self.list[self.front]
            self.list[self.front] = None
            return temp
        else:
            print("Queue is underflow!")

    def peek(self):
        if not self.isEmpty():
            return self.list[(self.front + 1) % self.size]
        else:
            print("Queue is Empty!")

q = circleQueue(5)

q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
q.enQueue(5)
q.deQueue()
q.deQueue()
q.deQueue()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)