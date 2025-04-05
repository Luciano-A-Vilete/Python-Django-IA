import unittest
from advanced_structures import binary_search, Stack, Queue

class TestAdvancedStructures(unittest.TestCase):
    def test_binary_search_found(self):
        sorted_list = [1, 3, 5, 7, 9]
        target = 7
        # The target 7 should be at index 3
        self.assertEqual(binary_search(sorted_list, target), 3)

    def test_binary_search_not_found(self):
        sorted_list = [1, 3, 5, 7, 9]
        target = 8
        # The target 8 is not in the list, so binary_search should return -1
        self.assertEqual(binary_search(sorted_list, target), -1)

    def test_stack_push_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        # The last element pushed should be popped first
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        # Test that popping from an empty stack raises an error
        with self.assertRaises(IndexError):
            s.pop()

    def test_queue_enqueue_dequeue(self):
        q = Queue()
        q.enqueue('a')
        q.enqueue('b')
        self.assertEqual(q.dequeue(), 'a')
        self.assertEqual(q.dequeue(), 'b')
        # Test that dequeuing from an empty queue raises an error
        with self.assertRaises(IndexError):
            q.dequeue()

if __name__ == '__main__':
    unittest.main()
