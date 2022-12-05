'''
Starting Sequence
[W] [V]     [P]                    
[B] [T]     [C] [B]     [G]        
[G] [S]     [V] [H] [N] [T]        
[Z] [B] [W] [J] [D] [M] [S]        
[R] [C] [N] [N] [F] [W] [C]     [W]
[D] [F] [S] [M] [L] [T] [L] [Z] [Z]
[C] [W] [B] [G] [S] [V] [F] [D] [N]
[V] [G] [C] [Q] [T] [J] [P] [B] [M]
 1   2   3   4   5   6   7   8   9 
'''

from dataclasses import dataclass, field


@dataclass
class Cargo:
  stacks: list[list[int]] = field(default_factory=list)

  def move(self, amount: int, stack: int, destination: int):
    for i in range(amount):
      crate = self.stacks[stack - 1].pop()
      self.stacks[destination - 1].append(crate)

  def move_multiple(self, amount: int, stack: int, destination: int):
    crates = []
    for i in range(amount):
      crate = self.stacks[stack - 1].pop()
      crates = [crate, *crates]
    self.stacks[destination - 1] += crates

  def get_top_crates(self) -> str:
    crates = ""
    for stack in self.stacks:
      crates += stack[-1]
    return crates
  
def solve():
  input = open("inputs/day5.txt", "r")
  steps = input.read().replace(" ", "").replace("move", "").replace("from", ";").replace("to", ";").split('\n')
  cargo = Cargo()
  cargo.stacks = [
    [*"VCDRZGBW"],
    [*"GWFCBSTV"],
    [*"CBSNW"],
    [*"QGMNJVCP"],
    [*"TSLFDHB"],
    [*"JVTWMN"],
    [*"PFLCSTG"],
    [*"BDZ"],
    [*"MNZW"],
  ]
  for step in steps:
    amount, stack, destination = step.split(";")
    cargo.move(int(amount), int(stack), int(destination))
  
  print(f"Top Crates: {cargo.get_top_crates()}")
  
  cargo = Cargo()
  cargo.stacks = [
    [*"VCDRZGBW"],
    [*"GWFCBSTV"],
    [*"CBSNW"],
    [*"QGMNJVCP"],
    [*"TSLFDHB"],
    [*"JVTWMN"],
    [*"PFLCSTG"],
    [*"BDZ"],
    [*"MNZW"],
  ]
  for step in steps:
    amount, stack, destination = step.split(";")
    cargo.move_multiple(int(amount), int(stack), int(destination))

  print(f"Top Crates (Multi Move): {cargo.get_top_crates()}")

if __name__ == "__main__":
  solve()