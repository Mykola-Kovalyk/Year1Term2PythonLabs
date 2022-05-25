from .binary_counter import BinaryCounter


class ReverseCounter(BinaryCounter):

    def __init__(self):
        super().__init__()

    def get_representation(self):
        return ''.join(['1' if x == '0' else '0' for x in super().get_representation()])

