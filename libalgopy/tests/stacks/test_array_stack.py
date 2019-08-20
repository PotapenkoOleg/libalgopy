from unittest import TestCase

from stacks.array_stack import ArrayStack


class TestsArrayStack(TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_pop(self):
        stack = ArrayStack()

        self.assertIsNone(stack.pop())
        expected = 42
        stack.push(expected + 2)
        stack.push(expected + 1)
        stack.push(expected)

        actual = stack.pop()
        self.assertEqual(expected, actual)

        actual = stack.pop()
        self.assertEqual(expected + 1, actual)

        actual = stack.pop()
        self.assertEqual(expected + 2, actual)

    def test_push(self):
        stack = ArrayStack()
        expected = 42
        stack.push(expected)
        stack.push(expected + 1)
        actual = stack.pop()
        self.assertEqual(expected + 1, actual)

    def test_peek(self):
        stack = ArrayStack()
        self.assertIsNone(stack.peek())

        expected = 42
        stack.push(expected + 2)
        stack.push(expected + 1)
        stack.push(expected)

        self.assertEqual(3, stack.get_size())

        actual = stack.peek()
        self.assertEqual(expected, actual)

        self.assertEqual(3, stack.get_size())

        actual = stack.pop()
        self.assertEqual(expected, actual)

    def test_clear(self):
        stack = ArrayStack()
        self.assertTrue(stack.is_empty())

        expected = 42
        stack.push(expected + 2)
        stack.push(expected + 1)
        stack.push(expected)

        self.assertFalse(stack.is_empty())
        self.assertEqual(3, stack.get_size())

        stack.clear()

        self.assertTrue(stack.is_empty())
        self.assertEqual(0, stack.get_size())
        self.assertIsNone(stack.pop())

    def test_is_empty(self):
        stack = ArrayStack()
        actual = stack.is_empty()
        self.assertTrue(actual)

        stack.push(42)
        actual = stack.is_empty()
        self.assertFalse(actual)

    def test_get_size(self):
        stack = ArrayStack()
        expected = 0
        actual = stack.get_size()
        self.assertEqual(expected, actual)

        stack.push(42)
        stack.push(42)
        stack.push(42)
        stack.pop()

        expected = 2
        actual = stack.get_size()
        self.assertEqual(expected, actual)

    def test_iterator(self):
        stack = ArrayStack()
        expected = 42
        stack.push(expected)
        stack.push(expected + 1)

        iterator = stack.__iter__()
        actual1 = iterator.__next__()
        actual2 = iterator.__next__()
        self.assertEqual(expected + 1, actual1)
        self.assertEqual(expected, actual2)

    def test_str(self):
        stack = ArrayStack()
        stack.push(42)
        stack.push(43)
        stack.push(44)
        expected = "44\n43\n42"
        actual = str(stack)
        self.assertEqual(expected, actual)
