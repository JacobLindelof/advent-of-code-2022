from dataclasses import dataclass
from math import floor
from typing import Dict


@dataclass
class OperationResult:
  new_value: int
  destination_index: int


class Monkey:

  def __init__(
    self, 
    id: int,
    items: list[int] = [], 
    operation: str = None, 
    test: int = None,
    destination_if_true: int = None, 
    destination_if_false: int = None
  ) -> None:
    self.id = id
    self.items = items
    self.operation = operation
    self.test = test
    self.true_destination = destination_if_true
    self.false_destination = destination_if_false
    self.inspection_count = 0
  
  def process_item(self, item, worry_factor: int = None) -> OperationResult:
    old = item
    item = eval(self.operation)
    if worry_factor:
      item = item % worry_factor
    else:
      item = floor(item / 3)
    destination = self.true_destination if item % self.test == 0 else self.false_destination
    self.inspection_count += 1
    return OperationResult(item, destination)

  def __str__(self) -> str:
    return f"Monkey {self.id} | Items Inspected: {self.inspection_count} | Items: {self.items}"

def process_round(monkeys: list[Monkey], worry_factor: int) -> list[Monkey]:
  for monkey in monkeys:
    while len(monkey.items) > 0:
      item = monkey.items.pop(0)
      result = monkey.process_item(item, worry_factor)
      monkeys[result.destination_index].items.append(result.new_value)

  return monkeys
  

def calculate_monkey_business_level(monkeys: list[Monkey]) -> int:
  interaction_counts = []
  for monkey in monkeys:
    interaction_counts.append(monkey.inspection_count)

  interaction_counts.sort(reverse=True)
  return interaction_counts[0] * interaction_counts[1]


def solve():
  input = open("inputs/day11.txt", "r")

  monkeys = []
  test_factor = None
  current_monkey: Monkey = None

  for line in input.read().split("\n"):
    if "Monkey" in line:
      monkeys.append(Monkey(id=int(line.replace("Monkey ", "").replace(":", ""))))
      current_monkey = monkeys[-1]
    elif "Starting items:" in line:
      current_monkey.items = list(map(int, line.replace("  Starting items: ", "").split(', ')))
    elif "Operation" in line:
      current_monkey.operation = line.strip().replace("Operation: new = ", "")
    elif "Test" in line:
      test = int(line.strip().replace("Test: divisible by ", ""))
      current_monkey.test = test
      if not test_factor:
        test_factor = test
      else:
        test_factor *= test
    elif "true" in line:
      current_monkey.true_destination = int(line.strip().replace("If true: throw to monkey ", ""))
    elif "false" in line:
      current_monkey.false_destination = int(line.strip().replace("If false: throw to monkey ", ""))
    else:
      pass
    
  rounds = 10000
  for i in range(rounds):
    monkeys = process_round(monkeys, test_factor)


  for monkey in monkeys:
    print(monkey)

  monkey_business_level = calculate_monkey_business_level(monkeys)
  print(f"Monkey Business Level: {monkey_business_level}")

if __name__ == "__main__":
  solve()