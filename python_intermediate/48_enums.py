from enum import Enum

# class State(Enum):
#     OFF = 0
#     ON = 1

# state = State.ON

# if state == State.ON:
#     print("The lamp is on.")
#     print(State.ON.value)
# elif state == State.OFF:
#     print("The lamp is off.")

class Color(Enum):
    RED = "Red"
    BLUE = "Blue"
    GREEN = "Greed"

c = Color.RED

def check_color(color: Color):
    if color == Color.RED:
        print(color.value)
    elif color == color.BLUE:
        print(color.value)
    elif color == Color.GREEN:
        print(color.value)

check_color(Color.BLUE)