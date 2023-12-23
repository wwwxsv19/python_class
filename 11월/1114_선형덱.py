class lineDeque:
    def __init__(self, size):
        self.size = size
        self.list = [None] * self.size
        self.front = -1
        self.rear = self.size

    def isEmpty(self):
        return self.rear == self.size - 1 and self.front == -1

    def isFull(self):
        return self.rear - self.front == 1

    def getFront(self):
        if not self.isEmpty():
            return self.list[self.front + 1]
        else:
            print("Deque is underflow!")

    def getRear(self):
        if not self.isEmpty():
            return self.list[self.rear]
        else:
            print("Deque is underflow!")

    def addFront(self, item):
        if not self.isFull():
            self.front += 1
            self.list[self.front] = item
        else:
            print("Deque is overflow!")

    def addRear(self, item):
        if not self.isFull():
            self.rear -= 1
            self.list[self.rear] = item
        else:
            print("Deque is overflow!")

    def deleteFront(self):
        if not self.isEmpty():
            temp = self.list[self.front]
            self.list[self.front] = None
            self.front -= 1
            return temp
        else:
            print("Deque is underflow!")

    def deleteRear(self):
        if not self.isEmpty():
            temp = self.list[self.rear]
            self.list[self.rear] = None
            self.rear += 1
            return temp
        else:
            print("Deque is underflow!")

    def printDeque(self):
        print(self.list)

Deque = lineDeque(5)

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