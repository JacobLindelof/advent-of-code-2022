def check_pair_for_full_overlap(pair: str) -> bool:
  assignment_1, assignment_2 = pair.split(",")
  assignment_1_x, assignment_1_y = assignment_1.split("-")
  assignment_2_x, assignment_2_y = assignment_2.split("-")

  if int(assignment_1_x) <= int(assignment_2_x) and int(assignment_1_y) >= int(assignment_2_y):
    return True
  
  if int(assignment_2_x) <= int(assignment_1_x) and int(assignment_2_y) >= int(assignment_1_y):
    return True
  
  return False


def check_pair_for_any_overlap(pair: str) -> bool:
  assignment_1, assignment_2 = pair.split(",")
  assignment_1_x, assignment_1_y = assignment_1.split("-")
  assignment_2_x, assignment_2_y = assignment_2.split("-")

  if int(assignment_1_x) >= int(assignment_2_x) and int(assignment_1_x) <= int(assignment_2_y):
    return True

  if int(assignment_1_y) >= int(assignment_2_x) and int(assignment_1_y) <= int(assignment_2_y):
    return True

  if int(assignment_2_x) >= int(assignment_1_x) and int(assignment_2_x) <= int(assignment_1_y):
    return True

  if int(assignment_2_y) >= int(assignment_1_x) and int(assignment_2_y) <= int(assignment_1_y):
    return True

  return False


def solve():
  input = open("inputs/day4.txt", "r")
  pairs = input.read().split("\n")

  total_overlapping = 0
  for pair in pairs:
    overlapping = check_pair_for_full_overlap(pair)
    if overlapping:
      total_overlapping += 1

  print(f"Overlapping Pairs: {total_overlapping}")

  total_overlapping = 0
  for pair in pairs:
    overlapping = check_pair_for_any_overlap(pair)
    if overlapping:
      total_overlapping += 1

  print(f"Partial Overlapping Pairs: {total_overlapping}")


if __name__ == "__main__":
  solve()