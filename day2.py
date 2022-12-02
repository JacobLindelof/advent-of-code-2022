def get_game_result(opponent_score, player_score):
  if opponent_score == 1:
    if player_score == 1:
      return 3
    elif player_score == 2:
      return 6
    else:
      return 0
    
  
  elif opponent_score == 2:
    if player_score == 1:
      return 0
    elif player_score == 2:
      return 3
    else:
      return 6

  else:
    if player_score == 1:
      return 6
    elif player_score == 2:
      return 0
    else:
      return 3

def get_game_score(game: str) -> int:
  point_map = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
  }
  opponent, player = game.replace("\n", "").split(" ")

  opponent_score = point_map[opponent]
  player_score = point_map[player]
  game_score = get_game_result(opponent_score, player_score)

  game_score += player_score
  return game_score

def get_player_move(game: str):
  lose_map = {
    "A": "C",
    "B": "A",
    "C": "B",
  }
  win_map = {
    "A": "B",
    "B": "C",
    "C": "A",
  }
  opponent, player = game.replace("\n", "").split(" ")
  if player == "X":
    return lose_map[opponent]
  elif player == "Y":
    return opponent
  else:
    return win_map[opponent]

def solve():
  input = open("inputs/day2.txt", "r")
  games = input.readlines()
  
  score = 0
  for game in games:
    score += get_game_score(game)

  print(f"Total Score: {score}")

  score = 0
  for game in games:
    player_move = get_player_move(game)
    game = game.replace("\n", "")[:-1] + player_move
    score += get_game_score(game)

  print(f"Total Score Part 2: {score}")



if __name__ == "__main__":
  solve()