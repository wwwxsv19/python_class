class makeNewDeque:
    def __init__(self, size = 5):
        self.size = size
        self.list = [None] * size
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.rear == self.front

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def getFront(self):
        if not self.isEmpty():
            print(self.list[(self.front + 1) % self.size])

    def getRear(self):
        if not self.isEmpty():
            print(self.list[self.rear])

    def addFront(self, e):
        if not self.isFull():
            self.list[self.front] = e
            self.front = (self.front - 1 + self.size) % self.size
            print(self.list)

    def addRear(self, e):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.size
            self.list[self.rear] = e
            print(self.list)

    def deleteFront(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.size
            self.list[self.front] = None
            print(self.list)

    def deleteRear(self):
        if not self.isEmpty():
            self.list[self.rear] = None
            self.rear = (self.rear - 1 + self.size) % self.size
            print(self.list)

Deque = makeNewDeque()

Deque.addFront(1)
Deque.addFront(2)
Deque.addRear(4)
Deque.addRear(5)