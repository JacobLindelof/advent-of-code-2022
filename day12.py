def solve():
  input = open("inputs/day12.txt", "r")
  rows = input.read().split('\n')

  map_grid = [list(row) for row in rows]
  visited_grid = [[False for col in row] for row in rows]

  for y in range(len(map_grid)):
    for x in range(len(map_grid[0])):
      visited_grid[y]
      if map_grid[y][x] == "S":
        start = (x, y)
        map_grid[y][x] = "a"
      if map_grid[y][x] == "E":
        end = (x, y)
        map_grid[y][x] = "z"

  points = []
  a_scores = []
  points.append((0, end[0], end[1]))

  while points:
    points.sort()
    score, x, y = points.pop(0)

    if visited_grid[y][x]:
      continue

    visited_grid[y][x] = True
    
    if (x, y) == start:
      print(f"Shortest Path Distance: {score}")

    elevation = map_grid[y][x]
    if elevation == "a":
      a_scores.append(score)
    
    for point in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      new_x = x + point[0]
      new_y = y + point[1]
      try: 
        new_elevation = map_grid[new_y][new_x]
      except IndexError:
        continue
      if ord(new_elevation) - ord(elevation) < -1:
        continue

      points.append((score + 1, new_x, new_y))
  
  print(f"Shortest Path From Lowest Elevation: {min(a_scores)}")

if __name__ == "__main__":
  solve()