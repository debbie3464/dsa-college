"""Queue (FIFO) on a fixed-size array: simple version and circular version.

Topic: Queue ADT, array implementation
All operations are O(1).
"""


class SimpleQueue:
    """front and rear only move right, so freed slots are never reused.

    Formulas: empty front > rear | full rear == capacity - 1
              enqueue: rear += 1, then store | dequeue: read, then front += 1
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front = 0
        self.rear = -1

    def is_empty(self):
        return self.front > self.rear

    def is_full(self):
        return self.rear == self.capacity - 1

    def enqueue(self, x):
        if self.is_full():
            raise OverflowError("queue overflow")
        self.rear += 1
        self.arr[self.rear] = x

    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue underflow")
        x = self.arr[self.front]
        self.arr[self.front] = None
        self.front += 1
        return x

    def peek(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        return self.arr[self.front]

    def size(self):
        return self.rear - self.front + 1


class CircularQueue:
    """Indexes wrap around with %, so freed slots are reused.

    Formulas: next free slot (front + count) % capacity
              dequeue: read arr[front], front = (front + 1) % capacity
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front = 0                     # index of the oldest item
        self.count = 0                     # how many items are stored

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def enqueue(self, x):
        if self.is_full():
            raise OverflowError("queue overflow")
        rear = (self.front + self.count) % self.capacity
        self.arr[rear] = x
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue underflow")
        x = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return x

    def peek(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        return self.arr[self.front]

    def size(self):
        return self.count


if __name__ == "__main__":
    # Simple queue: slot 0 is wasted after a dequeue
    q = SimpleQueue(3)
    q.enqueue(7)
    q.enqueue(8)
    assert q.dequeue() == 7
    q.enqueue(9)
    try:
        q.enqueue(5)                       # "full" although slot 0 is free
        assert False, "should overflow"
    except OverflowError:
        pass

    # Circular queue: slot 0 is reused
    c = CircularQueue(3)
    c.enqueue(1)
    c.enqueue(2)
    assert c.dequeue() == 1
    c.enqueue(3)
    assert c.dequeue() == 2
    c.enqueue(4)
    assert c.arr == [4, None, 3]           # 4 wrapped into slot 0
    c.enqueue(5)
    assert c.is_full()
    try:
        c.enqueue(6)
        assert False, "should overflow"
    except OverflowError:
        pass
    assert [c.dequeue(), c.dequeue(), c.dequeue()] == [3, 4, 5]
    assert c.is_empty()
    print("queues: all tests passed")
