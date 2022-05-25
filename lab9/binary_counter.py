DEFAULT_COUNTER_VALUE = 36182

class BinaryCounter:

    def __init__(self):
        self._count = DEFAULT_COUNTER_VALUE

    def increment(self):
        self._count += 1

    def decrement(self):
        self._count -= 1

    def get_representation(self):
        return bin(self._count)[2:].zfill(32)

    def get_count(self):
        return self._count


