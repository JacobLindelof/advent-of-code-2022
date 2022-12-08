from collections import defaultdict
import copy
from dataclasses import dataclass


@dataclass
class Directory:
  files = list

@dataclass
class File:
  name: str
  size: int


def process_directory(directory: dict) -> int:
  size = 0
  for name, item in directory.items():
    if name != "parent":
      if isinstance(item, File):
        size += item.size
      else:
        size += process_directory(item)
  directory['size'] = size
  return size


def calculate_directory_sizes(filesystem):
  temp_filesystem = copy.deepcopy(filesystem)
  for directory_name, directory in temp_filesystem.items():
    process_directory(directory)
  return temp_filesystem


def get_directory_sizes(filesystem, directory_sizes = []):
  for name, item in filesystem.items():
    directory_sizes.append(item['size'])
    for dir_name, dir_item in item.items():
      if dir_name not in ["parent", "size"] and isinstance(dir_item, dict):
        get_directory_sizes({dir_name: dir_item}, directory_sizes)
  return directory_sizes
    

def solve():
  input = open("inputs/day7.txt", "r")
  filesystem = {
    "/": {}
  }
  current_directory: dict = filesystem

  commands = input.read().split("\n")
  command = commands.pop(0)
  total_size_of_all_files = 0
  total_directories = 0
  try:
    while True:
      if "$" in command:
        if "cd" in command:
          directory = command.replace("$ cd ", "")
          print("CHANGING DIRECTORY TO: " + directory)
          if directory == "..":
            current_directory = current_directory['parent']
          else:
            current_directory =  current_directory[directory]
          command = commands.pop(0)
        elif "ls" in command:
          print("LISTING DIRECTORY CONTENTS: " + command)
          command = commands.pop(0)
          while "$" not in command:
            if "dir" in command:
              print(f"PROCESSING DIRECTORY: {command}")
              directory = command.replace("dir ", "")
              current_directory[directory] = {"parent": current_directory}
              command = commands.pop(0)
              total_directories += 1
            else:
              print(f"PROCESSING FILE: {command}")
              size, name = command.split(" ")
              current_directory[name] = File(name = name, size = int(size))
              total_size_of_all_files += int(size)
              command = commands.pop(0)
          print(command)
  except IndexError as e:
    print("END")

  filesystem = calculate_directory_sizes(filesystem)
  sizes = get_directory_sizes(filesystem)
  total_size_of_dir_under_100k = 0
  for size in sizes:
    if size <= 100000:
      total_size_of_dir_under_100k += size

  print("Directory Sum Under 100k: " + str(total_size_of_dir_under_100k))
  free_space = 70000000 - total_size_of_all_files
  needed_space = 30000000 - free_space
  possible_directories = []
  for size in sizes:
    if size >= needed_space:
      possible_directories.append(size)
  print(f"Directory Size to Delete: {min(possible_directories)}")

if __name__ == "__main__":
  solve()