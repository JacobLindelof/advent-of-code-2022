from enum import Enum


class SignalType(Enum):
  MARKER = 1
  MESSAGE = 2


def process_signal(input: str, type: SignalType) -> int:
  signal_position = 0
  buffer = []
  for char in input:
    signal_position += 1
    buffer.append(char)
    
    if type == SignalType.MARKER:
      if len(buffer) > 4:
        buffer.pop(0)
      if check_marker(buffer):
        return signal_position
    
    if type == SignalType.MESSAGE:
      if len(buffer) > 14:
        buffer.pop(0)
      if check_message(buffer):
        return signal_position


def check_marker(buffer: list[str]) -> bool:
  if len(list(set(buffer))) == 4:
    return True
  return False


def check_message(buffer: list[str]) -> bool:
  if len(list(set(buffer))) == 14:
    return True
  return False

    
def solve():
  input = open("inputs/day6.txt", "r").read()
  start_of_packet = process_signal(input, SignalType.MARKER)
  print(start_of_packet)

  message = process_signal(input, SignalType.MESSAGE)
  print(message)

if __name__ == "__main__":
  solve()