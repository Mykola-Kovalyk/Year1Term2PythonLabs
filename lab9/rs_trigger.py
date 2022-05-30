

class RsTrigger:

    def __init__(self):
        self._state = False
        pass

    def get_state(self, setter: bool, reset: bool):

        if reset and setter:
            raise "Invalid input"

        if reset or setter:
            self._state = setter

        return self._state
