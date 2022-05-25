from .binary_counter import BinaryCounter


class BinaryDecimalCounter(BinaryCounter):

    def __init__(self):
        super().__init__()

    def get_representation(self):

        str_representation = ''

        for string in str(self._count):
            str_representation = str_representation \
                                 + ('-' if str_representation != '' else '') \
                                 + (bin(int(string))[2:].zfill(4))

        return str_representation
