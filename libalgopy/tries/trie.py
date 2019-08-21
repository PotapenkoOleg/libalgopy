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
        def next_level(self):
            return self.__nextLevel

        @next_level.setter
        def next_level(self, value):
            self.__nextLevel = value

    # endregion

    # region Init

    def __init__(self):
        self.__root = Trie.Node()

    # endregion

    # region Public Methods

    def put(self, key, value):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError

    def delete(self, key):
        raise NotImplementedError

    def contains(self, key):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError

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

    # endregion


if __name__ == '__main__':
    pass
