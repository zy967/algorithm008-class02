class MyCircularDeque:

    """
    This implementation is straight forward and easy. However, the pop(i) operation takes O(n) time.
    This can be improved by a pointer, pointing to the last element.
    Or maybe I can implement this by a double linked list
    """
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head = 0
        self.tail = 0
        self.capacity = k + 1
        self.data = [0 for _ in range(self.capacity)]


    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.head = (self.head - 1 + self.capacity) % self.capacity
            self.data[self.head] = value
            return True


    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.data[self.tail] = value
            self.tail = (self.tail + 1) % self.capacity
            return True


    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.head = (self.head + 1) % self.capacity
            return True


    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.tail = (self.tail - 1 + self.capacity) % self.capacity
            return True


    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            return self.data[self.head]


    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            return self.data[(self.tail - 1 + self.capacity) % self.capacity]


    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.head == self.tail


    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return (self.tail + 1) % self.capacity == self.head