

class RsTrigger:

    def __init__(self):
        self._state = False
        pass

    def get_state(self, s: bool, r: bool):

        if r and s:
            raise "Invalid input"

        if r or s:
            self._state = s

        return self._state
