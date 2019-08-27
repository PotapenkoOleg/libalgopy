from unittest import TestCase

from tries.ternary_trie import TernaryTrie


def init_symbol_table():
    symbol_table = TernaryTrie()
    symbol_table.put("she", 0)
    symbol_table.put("sells", 1)
    symbol_table.put("sea", 2)
    symbol_table.put("shells", 3)
    symbol_table.put("by", 4)
    symbol_table.put("the", 5)
    symbol_table.put("sea", 6)
    symbol_table.put("shore", 7)
    symbol_table.put("a", 8)
    return symbol_table


class TestsTernaryTrie(TestCase):
    def test_put(self):
        symbol_table = init_symbol_table()

        expected = 8
        actual = symbol_table.get("a")
        self.assertEqual(expected, actual)

        expected = 4
        actual = symbol_table.get("by")
        self.assertEqual(expected, actual)

        expected = 6
        actual = symbol_table.get("sea")
        self.assertEqual(expected, actual)

        expected = 1
        actual = symbol_table.get("sells")
        self.assertEqual(expected, actual)

        expected = 0
        actual = symbol_table.get("she")
        self.assertEqual(expected, actual)

        expected = 3
        actual = symbol_table.get("shells")
        self.assertEqual(expected, actual)

        expected = 7
        actual = symbol_table.get("shore")
        self.assertEqual(expected, actual)

        expected = 5
        actual = symbol_table.get("the")
        self.assertEqual(expected, actual)

    def test_get(self):
        symbol_table = init_symbol_table()

        expected = 8
        actual = symbol_table.get("a")
        self.assertEqual(expected, actual)

        expected = 4
        actual = symbol_table.get("by")
        self.assertEqual(expected, actual)

        expected = 6
        actual = symbol_table.get("sea")
        self.assertEqual(expected, actual)

        expected = 1
        actual = symbol_table.get("sells")
        self.assertEqual(expected, actual)

        expected = 0
        actual = symbol_table.get("she")
        self.assertEqual(expected, actual)

        expected = 3
        actual = symbol_table.get("shells")
        self.assertEqual(expected, actual)

        expected = 7
        actual = symbol_table.get("shore")
        self.assertEqual(expected, actual)

        expected = 5
        actual = symbol_table.get("the")
        self.assertEqual(expected, actual)

        # invalid entry
        actual = symbol_table.get("invalid")
        self.assertIsNone(actual)

    def test_delete(self):
        symbol_table = init_symbol_table()

        # clear all entries
        symbol_table.delete("she")
        symbol_table.delete("sells")
        symbol_table.delete("sea")
        symbol_table.delete("shells")
        symbol_table.delete("by")
        symbol_table.delete("the")
        symbol_table.delete("sea")
        symbol_table.delete("shore")
        symbol_table.delete("a")

        expected = 0
        actual = symbol_table.get_size()
        self.assertEqual(expected, actual)

        symbol_table = init_symbol_table()

        symbol_table.delete("by")
        actual = symbol_table.get("by")
        self.assertIsNone(actual)

        symbol_table.delete("shore")
        actual = symbol_table.get("shore")
        self.assertIsNone(actual)

        expected = 3
        actual = symbol_table.get("shells")
        self.assertEqual(expected, actual)

        expected = 6
        actual = symbol_table.get("sea")
        self.assertEqual(expected, actual)

        symbol_table.delete("sea")
        expected = 1
        actual = symbol_table.get("sells")
        self.assertEqual(expected, actual)

        # invalid entry
        symbol_table.delete("by")
        actual = symbol_table.get("by")
        self.assertIsNone(actual)

        # delete root
        symbol_table.clear()
        symbol_table.put("a", 0)
        symbol_table.delete("a")
        actual = symbol_table.get("a")
        self.assertIsNone(actual)
        expected = 0
        actual = symbol_table.get_size()
        self.assertEqual(expected, actual)

    def test_clear(self):
        symbol_table = init_symbol_table()

        actual = symbol_table.is_empty()
        self.assertFalse(actual)

        symbol_table.clear()
        actual = symbol_table.is_empty()
        self.assertTrue(actual)

    def test_is_empty(self):
        symbol_table = init_symbol_table()

        actual = symbol_table.is_empty()
        self.assertFalse(actual)

        symbol_table.clear()
        actual = symbol_table.is_empty()
        self.assertTrue(actual)

        symbol_table.put("placeholder", 42)
        actual = symbol_table.is_empty()
        self.assertFalse(actual)

    def test_get_size(self):
        symbol_table = init_symbol_table()

        expected = 8
        actual = symbol_table.get_size()
        self.assertEqual(expected, actual)

        symbol_table.delete("by")
        expected = 7
        actual = symbol_table.get_size()
        self.assertEqual(expected, actual)

        symbol_table.clear()
        expected = 0
        actual = symbol_table.get_size()
        self.assertEqual(expected, actual)

    def test_get_all_keys(self):
        self.fail()

    def test_get_keys_with_prefix(self):
        self.fail()

    def test_wildcard_match(self):
        self.fail()

    def test_longest_prefix_of(self):
        self.fail()
