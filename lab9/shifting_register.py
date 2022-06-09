

class ShiftingRegister:

    def __init__(self):
        self._word = ""

    def store_new(self, value: bool):
        self._word = str(int(value)) + self._word

    def get_word(self):
        return self._word

    def reset(self):
        self._word = ''
