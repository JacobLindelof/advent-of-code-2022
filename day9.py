from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Point:
  x: int = 0
  y: int = 0

def visualize_rope(w, h, rope):
  grid = [["." for x in range(w * 2)] for y in range(h * 2)]

  for i in range(len(rope)):
    point = rope[i]
    if i == 0:
      marker = "H"
    else:
      marker = i

    if grid[point.y + h][point.x + w] == ".":
      grid[point.y + h][point.x + w] = marker

  if grid[h][w] == ".":
      grid[h][w] = "s"
  
  print(rope)
  for row in grid:
    print("".join(map(str, row)))

def solve():
  input = open("inputs/day9.txt", "r")
  moves = input.read().split("\n")
  # moves = [
  #   "R 4",
  #   "U 4",
  #   "L 3",
  #   "D 1",
  #   "R 4",
  #   "D 1",
  #   "L 5",
  #   "R 2"
  # ]
  
  h_pos = Point()
  t_pos = Point()
  visited = defaultdict(int)

  for move in moves:
    direction, length = move.split(" ")
    for i in range(int(length)):
      if direction == "U":
        h_pos.y += 1
      elif direction == "D":
        h_pos.y -= 1
      elif direction == "L":
        h_pos.x -= 1
      else: # Direction must be right
        h_pos.x += 1
      
      x_difference = h_pos.x - t_pos.x
      y_difference = h_pos.y - t_pos.y

      if x_difference == -2:
        t_pos.x -= 1
        if y_difference == -1:
          t_pos.y -= 1
        if y_difference == 1:
          t_pos.y += 1
      elif x_difference == 2:
        t_pos.x += 1
        if y_difference == -1:
          t_pos.y -= 1
        if y_difference == 1:
          t_pos.y += 1

      if y_difference == -2:
        t_pos.y -= 1
        if x_difference == -1:
          t_pos.x -= 1
        if x_difference == 1:
          t_pos.x += 1
      elif y_difference == 2:
        t_pos.y += 1
        if x_difference == -1:
          t_pos.x -= 1
        if x_difference == 1:
          t_pos.x += 1
      
      visited[f"{t_pos.x},{t_pos.y}"] += 1

  print(f"Points Visited: {len(visited.keys())}")
  
  rope = [Point() for i in range(10)]
  visited = defaultdict(int)

  # moves = [
  #   "R 5",
  #   "U 8",
  #   "L 8",
  #   "D 3",
  #   "R 17",
  #   "D 10",
  #   "L 25",
  #   "U 20",
  # ]

  for move in moves:
    direction, length = move.split(" ")
    for i in range(int(length)):
      head = rope[0]
      if direction == "U":
        head.y += 1
      elif direction == "D":
        head.y -= 1
      elif direction == "L":
        head.x -= 1
      else: # Direction must be right
        head.x += 1
      
      for i in range(1,10):
        head = rope[i - 1]
        point = rope[i]

        x_difference = head.x - point.x
        y_difference = head.y - point.y

        if x_difference == -2:
          point.x -= 1
          if y_difference == -1:
            point.y -= 1
          if y_difference == 1:
            point.y += 1
        elif x_difference == 2:
          point.x += 1
          if y_difference == -1:
            point.y -= 1
          if y_difference == 1:
            point.y += 1

        if y_difference == -2:
          point.y -= 1
          if x_difference == -1:
            point.x -= 1
          if x_difference == 1:
            point.x += 1
        elif y_difference == 2:
          point.y += 1
          if x_difference == -1:
            point.x -= 1
          if x_difference == 1:
            point.x += 1

      visited[f"{rope[-1].x},{rope[-1].y}"] += 1

  print(f"Points Visited: {len(visited.keys())}")

if __name__ == "__main__":
  solve()