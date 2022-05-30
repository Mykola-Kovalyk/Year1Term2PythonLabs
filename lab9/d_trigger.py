from .rs_trigger import RsTrigger


class DTrigger(RsTrigger):

    def __init__(self):
        super().__init__()

    def set_state(self, data: bool):
        self._state = data

    def get_state(self, setter=False, reset=False):
        return super().get_state(setter, reset)
