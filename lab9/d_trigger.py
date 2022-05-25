from .rs_trigger import RsTrigger


class DTrigger(RsTrigger):

    def __init__(self):
        super().__init__()

    def set_state(self, d: bool):
        self._state = d

    def get_state(self, s=False, r=False):
        return super().get_state(s, r)
