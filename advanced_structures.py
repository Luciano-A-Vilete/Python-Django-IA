# advanced_structures.py

class Stack:
    """
    A simple implementation of a stack (LIFO).
    """
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the stack."""
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top item of the stack.
        Raises IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def is_empty(self):
        """Return True if the stack is empty, otherwise False."""
        return len(self.items) == 0

    def peek(self):
        """Return the top item of the stack without removing it."""
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)


class Queue:
    """
    A simple implementation of a queue (FIFO).
    """
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the front item of the queue.
        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def is_empty(self):
        """Return True if the queue is empty, otherwise False."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)


def binary_search(sorted_list, target):
    """
    Performs binary search on a sorted list.

    Parameters:
        sorted_list (list): A list of items in sorted order.
        target: The item to search for.

    Returns:
        int: The index of the target in the list, or -1 if not found.
    """
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    # Demonstrate Stack functionality
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Stack top element:", s.peek())
    print("Stack size before pop:", s.size())
    print("Item popped from stack:", s.pop())
    print("Stack size after pop:", s.size())

    # Demonstrate Queue functionality
    q = Queue()
    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')
    print("Queue size:", q.size())
    print("Item dequeued from queue:", q.dequeue())
    print("Queue size after dequeue:", q.size())

    # Demonstrate binary search
    sorted_list = [1, 3, 5, 7, 9, 11]
    target = 7
    index = binary_search(sorted_list, target)
    if index != -1:
        print(f"Binary search: Found target {target} at index {index}")
    else:
        print("Target not found")
