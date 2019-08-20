from common.interfaces.stack import Stack


class ArrayStack(Stack):

    # region Init

    def __init__(self):
        self.__array = []
        self.__size = 0

    # endregion

    # region Public Methods

    def pop(self):
        if self.__size == 0:
            return None
        result = self.__array[-1]
        del self.__array[-1]
        self.__size -= 1
        return result

    def push(self, item):
        self.__array.append(item)
        self.__size += 1

    def peek(self):
        if self.__size == 0:
            return None
        return self.__array[-1]

    def clear(self):
        self.__size = 0
        self.__array = []

    def is_empty(self):
        return self.__size == 0

    def get_size(self):
        return self.__size

    # endregion

    # region Iterator

    def __iter__(self):
        self.__current = self.__size
        return self

    def __next__(self):
        if self.__current > 0:
            self.__current -= 1
            return self.__array[self.__current]
        else:
            raise StopIteration

    # endregion

    # region Str And Repr

    def __str__(self):
        return "\n".join([str(x) for x in self])

    def __repr__(self):
        return self.__str__()

    # endregion


if __name__ == '__main__':
    pass
