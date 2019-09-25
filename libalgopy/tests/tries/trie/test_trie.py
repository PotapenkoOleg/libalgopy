from unittest import TestCase

from tries.trie.trie import Trie


def init_symbol_table():
    symbol_table = Trie()
    symbol_table.put("a", 8)
    symbol_table.put("sea", 2)
    symbol_table.put("by", 4)
    symbol_table.put("sea", 6)
    symbol_table.put("sells", 1)
    symbol_table.put("she", 0)
    symbol_table.put("shells", 3)
    symbol_table.put("shore", 7)
    symbol_table.put("the", 5)
    return symbol_table


class TestsTrie(TestCase):
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

        symbol_table.delete("a")
        actual = symbol_table.get("a")
        self.assertIsNone(actual)

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
        symbol_table = init_symbol_table()
        hash_map = {
            "she": 0,
            "sells": 0,
            "shells": 0,
            "by": 0,
            "the": 0,
            "sea": 0,
            "shore": 0,
            "a": 0
        }
        all_keys = symbol_table.get_all_keys()

        expected = 8
        actual = self.__check_keys(all_keys, hash_map)
        self.assertEqual(expected, actual)

    def test_get_keys_with_prefix(self):
        symbol_table = init_symbol_table()
        hash_map = {
            "she": 0,
            "sells": 0,
            "shells": 0,
            "sea": 0,
            "shore": 0
        }
        prefix = "s"

        all_keys = symbol_table.get_keys_with_prefix(prefix)

        expected = 5
        actual = self.__check_keys(all_keys, hash_map)
        self.assertEqual(expected, actual)

        hash_map = {
            "she": 0,
            "shells": 0,
            "shore": 0
        }
        prefix = "sh"

        all_keys = symbol_table.get_keys_with_prefix(prefix)

        expected = 3
        actual = self.__check_keys(all_keys, hash_map)
        self.assertEqual(expected, actual)

        prefix = "Invalid"

        all_keys = symbol_table.get_keys_with_prefix(prefix)
        self.assertIsNone(all_keys)

    def test_longest_prefix_of(self):
        symbol_table = init_symbol_table()

        expected = "shells"
        actual = symbol_table.longest_prefix_of("shellsort")
        self.assertEqual(expected, actual)

        expected = "a"
        actual = symbol_table.longest_prefix_of("a")
        self.assertEqual(expected, actual)

        expected = ""
        actual = symbol_table.longest_prefix_of("Invalid")
        self.assertEqual(expected, actual)

        symbol_table.clear()

        symbol_table.put("128", 0)
        symbol_table.put("128.112.055", 0)
        symbol_table.put("128.112.055.015", 0)
        symbol_table.put("128.112.136", 0)
        symbol_table.put("128.112.155.011", 0)
        symbol_table.put("128.112.155.013", 0)
        symbol_table.put("128.112", 0)
        symbol_table.put("128.222", 0)
        symbol_table.put("128.222.136", 0)

        expected = "128.112.136"
        actual = symbol_table.longest_prefix_of("128.112.136.011")
        self.assertEqual(expected, actual)

        expected = "128.112"
        actual = symbol_table.longest_prefix_of("128.112.100.016")
        self.assertEqual(expected, actual)

        expected = "128"
        actual = symbol_table.longest_prefix_of("128.166.123.045")
        self.assertEqual(expected, actual)

        symbol_table.clear()
        symbol_table.put("a", 0)
        expected = "a"
        actual = symbol_table.longest_prefix_of("a")
        self.assertEqual(expected, actual)

    def __check_keys(self, all_keys, hash_map):
        number_of_items = 0
        for key in all_keys:
            number_of_items += 1
            value = hash_map[key]
            if value is None:
                self.fail("Invalid key")
        return number_of_items
