import copy


def render_map(map, sand_location = None):
  map_copy = copy.deepcopy(map)
  if sand_location:
    map_copy[sand_location[1]][sand_location[0]] = "O"
  for row in map_copy:
    print("".join(row))

def parse_map(paths: list[str], min_x: int, max_x: int, min_y: int, max_y: int):
  map = [
    [
      "." for x in range(max_x - min_x + 1)
    ] for y in range(max_y + 1)
  ]

  for path in paths:
    coordinates = [(int(coord.split(",")[0]) - min_x, int(coord.split(",")[1])) for coord in path.split(" -> ")]
    for i in range(len(coordinates) - 1):
      a, b = coordinates[i], coordinates[i + 1]
      x_difference = b[0] - a[0]
      y_difference = b[1] - a[1]

      for d in range(0, x_difference, -1 if x_difference < 0 else 1):
        map[a[1]][a[0] + d] = "#"
      for d in range(0, y_difference, -1 if y_difference < 0 else 1):
        map[a[1] + d][a[0]] = "#"
      
      map[b[1]][b[0]] = "#"
  return map


def drop_sand(rock_map: list[list[str]], sand_spawn: tuple):
  max_y= len(rock_map)
  max_x = len(rock_map[0])

  sand_location = sand_spawn
  sand_stuck = False
  while not sand_stuck:
    if sand_location[1] == max_y:
      return None
    else: 
      down = (sand_location[0], sand_location[1] + 1)
      left = (sand_location[0] - 1, sand_location[1] + 1) if sand_location[0] > 0 else None
      right = (sand_location[0] + 1, sand_location[1] + 1) if sand_location[0] < max_x - 1 else None

      if rock_map[down[1]][down[0]] == ".":
        sand_location = (down[0], down[1])

      elif not left:
        return None
      elif rock_map[left[1]][left[0]] == ".":
        sand_location = (left[0], left[1])

      elif not right:
        return None
      elif right and rock_map[right[1]][right[0]] == ".":
        sand_location = (right[0], right[1])

      else:
        sand_stuck = True
  
  return sand_location
      



def solve():
  input = open("inputs/day14.txt", "r").read()
  coordinates = input.replace("\n", " -> ").split(" -> ")
  x_coordinates = [int(coord.split(",")[0]) for coord in coordinates]
  y_coordinates = [int(coord.split(",")[1]) for coord in coordinates]
  min_x, max_x, min_y, max_y = min(x_coordinates), max(x_coordinates), min(y_coordinates), max(y_coordinates)

  paths = input.split("\n")
  rock_map = parse_map(paths, min_x, max_x, min_y, max_y)
  sand_spawn = (500 - min_x, 0)

  
  total_sand = 1
  sand_location = drop_sand(rock_map, sand_spawn)
  rock_map[sand_location[1]][sand_location[0]] = "O"

  while sand_location:
    sand_location = drop_sand(rock_map, sand_spawn)
    if sand_location:
      total_sand += 1
      rock_map[sand_location[1]][sand_location[0]] = "O"

  print(f"Total Sand Blocks: {total_sand}")

  render_map(rock_map)



if __name__ == "__main__":
  solve()