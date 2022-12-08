def check_visibility(x, y, forest_width, forest_height, forest):
  if x == 0 or x == forest_width - 1 or y == 0 or y == forest_height - 1:
    return True
  
  tree = forest[y][x]
  left_trees = forest[y][:x]
  right_trees = forest[y][x + 1:]
  top_trees = [row[x] for row in forest[:y]]
  bottom_trees = [row[x] for row in forest[y + 1:]]
  adjacent_trees = [left_trees, right_trees, top_trees, bottom_trees]
  
  visible = False
  for direction in adjacent_trees:
    if max(direction) < tree:
      visible = True
    
  return visible


def get_senic_score(x, y, forest):  
  tree = forest[y][x]
  left_trees = forest[y][:x]
  right_trees = forest[y][x + 1:]
  top_trees = [row[x] for row in forest[:y]]
  bottom_trees = [row[x] for row in forest[y + 1:]]
  adjacent_trees = [list(reversed(left_trees)), right_trees, list(reversed(top_trees)), bottom_trees]

  senic_score = None
  for direction in adjacent_trees:
    visible_trees = 0

    if len(direction) == 0:
      return 0 
      
    while len(direction) > 0:
      compare_tree = direction.pop(0)
      visible_trees += 1
      if compare_tree >= tree:
        direction = []

    if not senic_score:
      senic_score = visible_trees
    else:
      senic_score *= visible_trees
    
  return senic_score

def solve():
  input = open("inputs/day8.txt", "r")
  trees = input.read().split("\n")
  
  forest = [list(row) for row in trees]
  forest_width = len(forest)
  forest_height = len(forest[0])

  visible_trees = 0
  highest_senic_score = 0

  for y in range(forest_width):
    for x in range(forest_height):
      visible = check_visibility(x, y, forest_width, forest_height, forest)
      visible_trees += 1 if visible else 0

      senic_score = get_senic_score(x, y, forest)
      highest_senic_score = senic_score if senic_score > highest_senic_score else highest_senic_score
  
  print(f"Visible Trees: {visible_trees}")
  print(f"Highest Senic Score: {highest_senic_score}")

if __name__ == "__main__":
  solve()