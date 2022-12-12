from math import floor


class Screen:

  def __init__(self, width = 40, height = 6) -> None:
    self.display = [["" for w in range(width)] for h in range(height)]

  def draw(self, cycle, x):
    row = floor((cycle - 1) / 40)
    pixel = cycle % 40
    if pixel == 0:
      pixel = 40
    
    if pixel - 1 in range(x - 1, x + 2):
      self.display[row][pixel - 1] = "#"
    else:
      self.display[row][pixel - 1] = "."

  def render(self):
    for row in self.display:
      print(row)

class Processor:

  def __init__(self, enable_logging = True, first_log = 20, log_interval = 40, screen: Screen = None) -> None:
    self.cycle = 0
    self.x = 1
    self.total_signal_strength = 0
    self.logging = enable_logging
    self.first_log = first_log
    self.log_interval = log_interval
    self.screen = screen

  def signal_strength(self):
    return self.cycle * self.x

  def increment_cycle(self, count: int = 1):
    for i in range(count):
      self.cycle += 1
      if self.screen:
        self.screen.draw(self.cycle, self.x)
      if self.cycle == self.first_log or (self.cycle - self.first_log) % self.log_interval == 0:
        self.total_signal_strength += self.signal_strength()
        if self.logging:
          print(f"Signal Strength @ Cycle {self.cycle}: {self.signal_strength()}")

  def noop(self):
    self.increment_cycle()
    return

  def addx(self, value: int):
    self.increment_cycle(2)
    self.x += value


def solve():
  input = open("inputs/day10.txt", "r")
  instructions = input.read().split("\n")

  screen = Screen()
  processor = Processor(enable_logging=False,screen=screen)

  for instruction in instructions:
    if instruction == "noop":
      processor.noop()
    else:
      operation, value = instruction.split(" ")
      processor.addx(int(value))
  
  print(f"Processor Signal Strength: {processor.total_signal_strength}")
  screen.render()


if __name__ == "__main__":
  solve()