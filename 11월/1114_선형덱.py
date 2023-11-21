class makeNewDeque:
    def __init__(self, size = 5):
        self.size = size
        self.list = [None] * size
        self.front = -1
        self.rear = self.size

    def isEmpty(self):
        return self.rear == self.size - 1 and self.front == -1

    def isFull(self):
        return self.rear - self.front == 1

    def getFront(self):
        if not self.isEmpty():
            print(self.list[self.front + 1])

    def getRear(self):
        if not self.isEmpty():
            print(self.list[self.rear])

    def addFront(self, e):
        if not self.isFull():
            self.front += 1
            self.list[self.front] = e
            print(self.list)
        else:
            print("Deque is overflow!")

    def addRear(self, e):
        if not self.isFull():
            self.rear -= 1
            self.list[self.rear] = e
            print(self.list)
        else:
            print("Deque is overflow!")

    def deleteFront(self):
        if not self.isEmpty():
            self.list[self.front] = None
            self.front -= 1
            print(self.list)
        else:
            print("Deque is underflow!")

    def deleteRear(self):
        if not self.isEmpty():
            self.list[self.rear] = None
            self.rear += 1
            print(self.list)
        else:
            print("Deque is underflow!")

Deque = makeNewDeque()

Deque.addFront(1)
Deque.addFront(2)
Deque.addRear(3)
Deque.addRear(4)
Deque.addRear(5)
Deque.addRear(6)
Deque.deleteFront()
Deque.deleteRear()
Deque.deleteFront()
Deque.deleteRear()
Deque.deleteFront()