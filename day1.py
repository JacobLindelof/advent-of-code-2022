from dataclasses import dataclass, field
from io import FileIO

@dataclass
class Elf:
    inventory: list[int] = field(default_factory=list)

    @property
    def total_calories(self) -> int:
        return sum(self.inventory)

def parse_elves(input: FileIO):
    elves: list[Elf] = []
    elf = Elf()
    for line in input.readlines():
        if line == "\n":
            elves.append(elf)
            elf = Elf()
        else:
            elf.inventory.append(int(line))
    elves.append(elf)
    
    return elves

def get_elf_with_most_calories(elves: list[Elf]) -> Elf:
    elf_with_most_calories = None
    for elf in elves:
        if not elf_with_most_calories or elf.total_calories > elf_with_most_calories.total_calories:
            elf_with_most_calories = elf
    return elf_with_most_calories

def get_elves_sorted_by_carried_calories(elves: list[Elf]) -> list[Elf]:
    elves = elves.copy()
    elves.sort(key=lambda elf: elf.total_calories)
    elves.reverse()
    return elves


def solve() -> None:
    input = open('inputs/day1.txt', "r")
    
    elves: list[Elf] = parse_elves(input)

    elf_with_most_calories = get_elf_with_most_calories(elves)
    print(f'Elf With Most Calories: {elf_with_most_calories.total_calories}')

    sorted_elves = get_elves_sorted_by_carried_calories(elves)
    print(f'Top 3 Elves: {sorted_elves[0].total_calories}, {sorted_elves[1].total_calories}, {sorted_elves[2].total_calories} | Total Calories: {sum(elf.total_calories for elf in sorted_elves[:3])}')

if __name__ == "__main__":
    solve()