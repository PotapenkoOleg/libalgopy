from unittest import TestCase

from heaps.array_binary_heap import ArrayBinaryHeap


class TestsArrayBinaryHeap(TestCase):
    def test_insert(self):
        priority_queue = ArrayBinaryHeap()
        test_data = "TPRNHOAEIG"
        for i in range(len(test_data)):
            current = test_data[i]
            priority_queue.insert(current)
        priority_queue.insert('S')
        priority_queue.delete()
        priority_queue.delete()
        priority_queue.insert('S')

        actual = ""
        for i in range(len(test_data)):
            actual += priority_queue.delete()

        expected = "SRPONIHGEA"
        self.assertEqual(expected, actual)

    def test_delete(self):
        priority_queue = ArrayBinaryHeap()
        self.assertIsNone(priority_queue.delete())

        test_data = "GIEAOHNRPT"
        for i in range(len(test_data)):
            current = test_data[i]
            priority_queue.insert(current)

        actual = ""
        for i in range(len(test_data)):
            actual += priority_queue.delete()

        expected = "TRPONIHGEA"
        self.assertEqual(expected, actual)

    def test_peek(self):
        priority_queue = ArrayBinaryHeap()
        self.assertIsNone(priority_queue.peek())

        test_data = "GIEAOHNRPT"
        for i in range(len(test_data)):
            current = test_data[i]
            priority_queue.insert(current)

        expected = 'T'
        actual = priority_queue.peek()
        self.assertEqual(expected, actual)

    def test_is_empty(self):
        priority_queue = ArrayBinaryHeap()
        self.assertTrue(priority_queue.is_empty())

        test_data = "GIEAOHNRPT"
        for i in range(len(test_data)):
            current = test_data[i]
            priority_queue.insert(current)

        self.assertFalse(priority_queue.is_empty())

    def test_get_size(self):
        priority_queue = ArrayBinaryHeap()
        actual = priority_queue.get_size()
        self.assertEqual(0, actual)

        test_data = "GIEAOHNRPT"
        for i in range(len(test_data)):
            current = test_data[i]
            priority_queue.insert(current)

        expected = 10
        actual = priority_queue.get_size()
        self.assertEqual(expected, actual)

    def test_clear(self):
        priority_queue = ArrayBinaryHeap()
        self.assertTrue(priority_queue.is_empty())

        test_data = "GIEAOHNRPT"
        for i in range(len(test_data)):
            current = test_data[i]
            priority_queue.insert(current)

        self.assertFalse(priority_queue.is_empty())

        priority_queue.clear()
        self.assertTrue(priority_queue.is_empty())

        expected = 0
        actual = priority_queue.get_size()
        self.assertEqual(expected, actual)
