"""Stack (LIFO) built on a fixed-size array with a `top` index.

Topic: Stack ADT, array implementation
Formulas: empty top == -1 | full top == capacity - 1
          push: top += 1, then store | pop: read, then top -= 1
All operations are O(1).
"""


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.top = -1                      # -1 means empty

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, x):
        if self.is_full():
            raise OverflowError("stack overflow")
        self.top += 1                      # move first
        self.arr[self.top] = x             # then store

    def pop(self):
        if self.is_empty():
            raise IndexError("stack underflow")
        x = self.arr[self.top]             # read first
        self.arr[self.top] = None
        self.top -= 1                      # then move
        return x

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.arr[self.top]

    def size(self):
        return self.top + 1


if __name__ == "__main__":
    s = Stack(3)
    assert s.is_empty()
    s.push(5)
    s.push(8)
    s.push(2)
    assert s.is_full() and s.size() == 3
    try:
        s.push(1)
        assert False, "should overflow"
    except OverflowError:
        pass
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.pop() == 8
    assert s.pop() == 5
    assert s.is_empty()
    try:
        s.pop()
        assert False, "should underflow"
    except IndexError:
        pass
    print("stack: all tests passed")
