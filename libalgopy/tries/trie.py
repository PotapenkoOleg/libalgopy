from common.interfaces.symbol_table import SymbolTable


class Trie(SymbolTable):
    # region Node Class

    class Node:
        def __init__(self):
            self.__value = None
            self.__nextLevel = {}

        @property
        def value(self):
            return self.__value

        @value.setter
        def value(self, value):
            self.__value = value

        @property
        def next_level(self, index):
            return self.__nextLevel[index]

        @next_level.setter
        def next_level(self, value, next_node):
            self.__nextLevel[value] = next_node

    # endregion

    # region Init

    def __init__(self):
        self.__root = Trie.Node()

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
        self.__root = Trie.Node()

    def is_empty(self):
        return self.__is_level_empty(self.__root)

    def get_size(self):
        raise NotImplementedError

    def get_all_keys(self):
        raise NotImplementedError

    def get_keys_with_prefix(self, prefix):
        raise NotImplementedError

    def wildcard_match(self, key):
        raise NotImplementedError

    def longest_prefix_of(self, prefix):
        raise NotImplementedError

    # endregion

    # region Private Methods

    def __get(self, node, key, level_counter):
        if node is None:
            return None
        if level_counter == len(key):
            return node
        index = key[level_counter]
        next_level = node.next_level(index)
        return self.__get(next_level, key, level_counter + 1)

    def __put(self, node, key, value, level_counter):
        if node is None:
            node = Trie.Node()
        if level_counter == len(key):
            node.value = value
            return node
        index = key[level_counter]
        next_level = node.next_level(index)
        next_node = self.__put(next_level, key, value, level_counter + 1)
        node.next_level(index, next_node)
        return node

    def __delete(self, node, key, level_counter):
        pass

    def __is_level_empty(self, level):
        return len(level.next_level) > 0

    # endregion


if __name__ == '__main__':
    pass
