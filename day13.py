from functools import cmp_to_key

def compare(a, b):
  if type(a) == int and type(b) == int:
    if a < b:
      return -1
    if a == b:
      return 0
    if a > b:
      return 1

  elif type(a) == int:
    return compare([a], b)

  elif type(b) == int:
    return compare(a, [b])
          
  else:
    for x, y in zip(a, b):
      res = compare(x, y)
      if res != 0: 
        return res

    if len(a) < len(b):
      return -1
    if len(a) == len(b):
      return 0
    if len(a) > len(b):
      return 1
    
  return True


def solve():
  input = open("inputs/day13.txt", "r")
  signal_pairs = input.read().split("\n\n")

  all_signals = [[[2]], [[6]]]

  valid_pairs = []
  for i in range(len(signal_pairs)):
    a, b = signal_pairs[i].split("\n", 1)
    a = eval(a)
    b = eval(b)
    all_signals.append(a)
    all_signals.append(b)
    res = compare(a, b)
    if res < 1:
      valid_pairs.append(i + 1)
    
  all_signals.sort(key=cmp_to_key(compare))
  print(f"Sum of Valid Pair Indices: {sum(valid_pairs)}")
  print(f"Decoder Key: {(all_signals.index([[2]]) + 1) * (all_signals.index([[6]]) + 1)}")

  

if __name__ == "__main__":
  solve()