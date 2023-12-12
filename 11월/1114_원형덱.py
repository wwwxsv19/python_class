class circleDeque:
    def __init__(self, size):
        self.size = size
        self.list = [None] * self.size
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.rear == self.front

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def getFront(self):
        if not self.isEmpty():
            return self.list[(self.front + 1) % self.size]

    def getRear(self):
        if not self.isEmpty():
            return self.list[self.rear]

    def addFront(self, item):
        if not self.isFull():
            self.list[self.front] = item
            self.front = (self.front - 1 + self.size) % self.size

    def addRear(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.size
            self.list[self.rear] = item

    def deleteFront(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.size
            temp = self.list[self.front]
            self.list[self.front] = None
            return temp

    def deleteRear(self):
        if not self.isEmpty():
            temp = self.list[self.rear]
            self.list[self.rear] = None
            self.rear = (self.rear - 1 + self.size) % self.size
            return temp

Deque = circleDeque(5)

Deque.addFront(1)
Deque.addFront(2)
Deque.addRear(4)
Deque.addRear(5)