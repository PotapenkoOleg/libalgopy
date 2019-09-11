from common.interfaces.symbol_table import SymbolTable


class TernaryTrie(SymbolTable):
    # region Node Class

    class TernaryTrieNode:
        def __init__(self, character):
            self.__character = character
            self.__value = None
            self.__left = None
            self.__middle = None
            self.__right = None

        @property
        def character(self):
            return self.__character

        @property
        def value(self):
            return self.__value

        @value.setter
        def value(self, value):
            self.__value = value

        @property
        def left(self):
            return self.__left

        @left.setter
        def left(self, value):
            self.__left = value

        @property
        def middle(self):
            return self.__middle

        @middle.setter
        def middle(self, value):
            self.__middle = value

        @property
        def right(self):
            return self.__right

        @right.setter
        def right(self, value):
            self.__right = value

    # endregion

    # region Init

    def __init__(self):
        self.__root = None
        self.__size = 0

    # endregion

    # region Public Methods

    def put(self, key, value):
        self.__root = self.__put(self.__root, key, value, 0)

    def get(self, key):
        node = self.__get(self.__root, key, 0)
        if node is None:
            return None
        return node.value

    def delete(self, key):
        child = self.__delete(self.__root, key, 0)
        self.__set_child_to_none(self.__root, child)
        if self.__is_node_empty(self.__root):
            self.__root = None

    def contains(self, key):
        return self.get(key) is not None

    def clear(self):
        self.__root = None
        self.__size = 0

    def is_empty(self):
        return self.__root is None

    def get_size(self):
        return self.__size

    def get_all_keys(self):
        queue = []  # we don't use queue class here since python list implements queue
        self.__collect(self.__root, "", queue)
        return queue

    def get_keys_with_prefix(self, prefix):
        sub_tree = self.__get(self.__root, prefix, 0)
        if sub_tree is None:
            return None
        queue = []  # we don't use queue class here since python list implements queue
        self.__collect(sub_tree.middle, prefix, queue)
        return queue

    def longest_prefix_of(self, prefix):
        prefix_length = self.__search(self.__root, prefix, 0, -1)
        if prefix_length == -1:
            return None  # prefix not found
        result = prefix[0:prefix_length + 1]
        return result

    # endregion

    # region Private Methods

    def __put(self, node, key, value, level_counter):
        character = key[level_counter]
        if node is None:
            node = TernaryTrie.TernaryTrieNode(character)
        if character < node.character:
            node.left = self.__put(node.left, key, value, level_counter)
        elif character > node.character:
            node.right = self.__put(node.right, key, value, level_counter)
        elif level_counter < (len(key) - 1):
            node.middle = self.__put(node.middle, key, value, level_counter + 1)
        else:
            if node.value is None:
                self.__size += 1
            node.value = value
        return node

    def __get(self, node, key, level_counter):
        if node is None:
            return None
        character = key[level_counter]
        if character < node.character:
            return self.__get(node.left, key, level_counter)
        elif character > node.character:
            return self.__get(node.right, key, level_counter)
        elif level_counter < (len(key) - 1):
            return self.__get(node.middle, key, level_counter + 1)
        else:
            return node

    def __delete(self, node, key, level_counter):
        if node is None:
            return None
        character = key[level_counter]
        if character < node.character:
            child_node = self.__delete(node.left, key, level_counter)
            if (child_node is not None) and (self.__is_node_empty(child_node)):
                self.__set_child_to_none(node, child_node)
            return node
        elif character > node.character:
            child_node = self.__delete(node.right, key, level_counter)
            if (child_node is not None) and (self.__is_node_empty(child_node)):
                self.__set_child_to_none(node, child_node)
            return node
        elif level_counter < (len(key) - 1):
            child_node = self.__delete(node.middle, key, level_counter + 1)
            if (child_node is not None) and (self.__is_node_empty(child_node)):
                self.__set_child_to_none(node, child_node)
            return node
        else:
            node.value = None
            self.__size -= 1
            return node

    def __is_node_empty(self, node):
        return (node.value is None) and (self.__is_node_have_no_children(node))

    def __is_node_have_no_children(self, node):
        return (node.left is None) and (node.middle is None) and (node.right is None)

    def __set_child_to_none(self, parent, child):
        if parent is None:
            return
        if parent.left == child:
            parent.left = None
        if parent.middle == child:
            parent.middle = None
        if parent.right == child:
            parent.right = None

    def __collect(self, node, prefix, queue):
        if node is None:
            return
        self.__collect(node.left, prefix, queue)
        character = node.character
        if node.value is not None:
            queue.append(prefix + character)
        self.__collect(node.middle, prefix + character, queue)
        self.__collect(node.right, prefix, queue)

    def __search(self, node, query, level_counter, prefix_length):
        if node is None:
            return prefix_length
        character = query[level_counter]
        if character < node.character:
            return self.__search(node.left, query, level_counter, prefix_length)
        elif character > node.character:
            return self.__search(node.right, query, level_counter, prefix_length)
        else:
            if node.value is not None:
                prefix_length = level_counter
            return self.__search(node.middle, query, level_counter + 1, prefix_length)

    # endregion


if __name__ == '__main__':
    pass
