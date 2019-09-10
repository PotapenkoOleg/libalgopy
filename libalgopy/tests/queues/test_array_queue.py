from unittest import TestCase

from queues.array_queue import ArrayQueue


class TestsArrayQueue(TestCase):
    def test_enqueue(self):
        queue = ArrayQueue()

        expected = 42
        queue.enqueue(expected)
        queue.enqueue(expected - 1)
        queue.enqueue(expected - 2)

        actual = queue.dequeue()
        self.assertEqual(expected, actual)

    def test_dequeue(self):
        queue = ArrayQueue()

        self.assertIsNone(queue.dequeue())

        expected = 42
        queue.enqueue(expected)
        actual = queue.dequeue()
        self.assertEqual(expected, actual)

        queue.enqueue(expected)
        queue.enqueue(expected - 1)
        actual = queue.dequeue()
        self.assertEqual(expected, actual)

    def test_peek(self):
        queue = ArrayQueue()
        self.assertIsNone(queue.peek())

        expected = 42
        queue.enqueue(expected)
        actual = queue.peek()
        self.assertEqual(expected, actual)

        queue.clear()

        queue.enqueue(expected)
        queue.enqueue(expected - 1)
        actual = queue.peek()
        self.assertEqual(expected, actual)

    def test_clear(self):
        queue = ArrayQueue()
        actual = queue.get_size()
        self.assertEqual(0, actual)
        self.assertTrue(queue.is_empty())

        expected = 42
        queue.enqueue(expected)
        queue.enqueue(expected - 1)
        queue.enqueue(expected - 2)

        actual = queue.get_size()
        self.assertEqual(3, actual)
        self.assertFalse(queue.is_empty())

        queue.clear()

        actual = queue.get_size()
        self.assertEqual(0, actual)
        self.assertTrue(queue.is_empty())

    def test_is_empty(self):
        queue = ArrayQueue()
        actual = queue.is_empty()
        self.assertTrue(actual)

        queue.enqueue(42)
        actual = queue.is_empty()
        self.assertFalse(actual)

    def test_get_size(self):
        queue = ArrayQueue()
        expected = 0
        actual = queue.get_size()
        self.assertEqual(expected, actual)

        queue.enqueue(42)
        queue.enqueue(42)
        queue.enqueue(42)
        queue.dequeue()

        expected = 2
        actual = queue.get_size()
        self.assertEqual(expected, actual)
