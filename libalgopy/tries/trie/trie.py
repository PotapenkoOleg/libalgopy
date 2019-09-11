from common.interfaces.symbol_table import SymbolTable


class Trie(SymbolTable):
    NUMBER_OF_LETTERS_IN_EXTENDED_ASCII = 256

    # region Node Class

    class TrieNode:
        def __init__(self, number_of_letters):
            self.__value = None
            self.__nextLevel = [None for i in range(number_of_letters)]

        @property
        def value(self):
            return self.__value

        @value.setter
        def value(self, value):
            self.__value = value

        def get_next_level(self):
            return self.__nextLevel

        def get_next_level_at(self, index):
            return self.__nextLevel[index]

        def set_next_level_at(self, index, next_node):
            self.__nextLevel[index] = next_node

    # endregion

    # region Init

    def __init__(self, number_of_letters=NUMBER_OF_LETTERS_IN_EXTENDED_ASCII):
        self.__number_of_letters = number_of_letters
        self.__root = Trie.TrieNode(number_of_letters)
        self.__size = 0

    # endregion

    # region Public Methods

    def get(self, key):
        node = self.__get(self.__root, key, 0)
        if node is None:
            return None
        return node.value

    def put(self, key, value):
        self.__root = self.__put(self.__root, key, value, 0)

    def delete(self, key):
        self.__delete(self.__root, key, 0)

    def contains(self, key):
        return self.__get(key) is not None

    def clear(self):
        self.__root = Trie.TrieNode(Trie.NUMBER_OF_LETTERS_IN_EXTENDED_ASCII)
        self.__size = 0

    def is_empty(self):
        return self.__is_level_empty(self.__root)

    def get_size(self):
        return self.__size

    def get_all_keys(self):
        queue = []
        self.__collect(self.__root, "", queue)
        return queue

    def get_keys_with_prefix(self, prefix):
        sub_tree = self.__get(self.__root, prefix, 0)
        if sub_tree is None:
            return None
        queue = []  # we don't use queue class here since python list implements queue
        self.__collect(sub_tree, prefix, queue)
        return queue

    def longest_prefix_of(self, prefix):
        prefix_length = self.__search(self.__root, prefix, 0, 0)
        return prefix[0: prefix_length]

    # endregion

    # region Private Methods

    def __get(self, node, key, level_counter):
        if node is None:
            return None
        if level_counter == len(key):
            return node
        index = ord(key[level_counter])
        next_level = node.get_next_level_at(index)
        return self.__get(next_level, key, level_counter + 1)

    def __put(self, node, key, value, level_counter):
        if node is None:
            node = Trie.TrieNode(self.__number_of_letters)
        if level_counter == len(key):
            if node.value is None:
                self.__size += 1
            node.value = value
            return node
        index = ord(key[level_counter])
        next_level = node.get_next_level_at(index)
        next_node = self.__put(next_level, key, value, level_counter + 1)
        node.set_next_level_at(index, next_node)
        return node

    def __delete(self, node, key, level_counter):
        if node is None:
            return False
        if level_counter == len(key):
            node.value = None
            self.__size -= 1
        else:
            index = ord(key[level_counter])
            next_level = node.get_next_level_at(index)
            is_next_level_empty = self.__delete(next_level, key, level_counter + 1)
            if is_next_level_empty:
                node.set_next_level_at(index, None)
        return self.__is_level_empty(node)

    def __is_level_empty(self, level):
        return all(current is None for current in level.get_next_level())

    def __collect(self, node, prefix, queue):
        if node is None:
            return
        if node.value is not None:
            queue.append(prefix)
        for character in range(self.__number_of_letters - 1):
            next_level = node.get_next_level()
            self.__collect(next_level[character], prefix + chr(character), queue)

    def __search(self, node, query, level_counter, prefix_length):
        if node is None:
            return prefix_length
        if node.value is not None:
            prefix_length = level_counter
        if level_counter == len(query):
            return prefix_length
        character = query[level_counter]
        next_level = node.get_next_level()
        return self.__search(next_level[ord(character)], query, level_counter + 1, prefix_length)

    # endregion


if __name__ == '__main__':
    pass
