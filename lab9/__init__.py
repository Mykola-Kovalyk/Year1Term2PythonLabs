from .binary_decimal_counter import BinaryDecimalCounter
from .binary_counter import BinaryCounter
from .reverse_counter import ReverseCounter
from .rs_trigger import RsTrigger
from .d_trigger import DTrigger
from .multiplexer import Multiplexer
from .shifting_register import ShiftingRegister

def main():

    binary = BinaryCounter()
    bin_dec = BinaryDecimalCounter()
    reverse = ReverseCounter()

    rs = RsTrigger()
    d = DTrigger()

    shift_reg =  ShiftingRegister()

    inputs  = [True, False, False, True]
    multiplex = Multiplexer(inputs)

    binary.increment()
    bin_dec.increment()
    reverse.increment()

    print("Counters: ")
    print(f"binary for {binary.get_count()}: {binary.get_representation()}")
    print(f"binary-decimal for {binary.get_count()}: {bin_dec.get_representation()}")
    print(f"reversed for {binary.get_count()}: {reverse.get_representation()}")
    print("")

    print("RS-trigger: ")
    print(f"set is true: {rs.get_state(True, False)}")
    print(f"reset is true: {rs.get_state(False, True)}")
    print(f"set is true again: {rs.get_state(True, False)}")
    print(f"no change: {rs.get_state(False, False)}")
    print("")

    print("D-trigger:")
    d.set_state(True)
    print(f"state is True: {d.get_state()}")
    d.set_state(False)
    print(f"state is False: {d.get_state()}")
    print("")

    print(f"Multiplexer for inputs {inputs}:")
    print(f"Initial output: {multiplex.get_output()}")
    multiplex.select_input(2)
    print(f"Input at index 2 was selected: {multiplex.get_output()}")
    multiplex.set_input(2, True)
    print(f"Input at index 2 was changed to True: {multiplex.get_output()}")
    print("")

    print("Shifting register:")
    print(f"Initial word: {shift_reg.get_word()}")
    shift_reg.store_new(True)
    print(f"After storing 1: {shift_reg.get_word()}")
    shift_reg.store_new(False)
    print(f"After storing 0: {shift_reg.get_word()}")
    shift_reg.store_new(True)
    print(f"After storing 1: {shift_reg.get_word()}")
    shift_reg.store_new(True)
    print(f"After storing 1: {shift_reg.get_word()}")
    shift_reg.store_new(False)
    print(f"After storing 0: {shift_reg.get_word()}")
    shift_reg.reset()
    print(f"After reset: {shift_reg.get_word()}")



