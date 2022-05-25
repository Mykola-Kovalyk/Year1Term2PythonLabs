

class Multiplexer:

    def __init__(self, inputs: list[bool]):

        self._selected_input = 0
        self._inputs = inputs

    def set_input(self, input_index: int, value: bool):
        self._inputs[input_index] = value

    def select_input(self, input_index):
        if 0 <= input_index < len(self._inputs):
            self._selected_input = input_index
        else:
            raise f"Input index out of range, got {input_index}, must be between 0 and {len(self._inputs) - 1}"

    def get_output(self):
        return self._inputs[self._selected_input]

