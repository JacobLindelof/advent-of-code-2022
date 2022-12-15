from collections import defaultdict
import json

def render_map(map):
  for row in map:
    print("".join(row))

def solve():
  input = open("inputs/day15.txt", "r").read()
  check_row = 2000000
  inelegible_positions = []
  beacons_on_row = []

  search_size = 4000000
  beacon_map = defaultdict(list)
  
  for row in input.split("\n"):
    print(row) 
    sensor, beacon = row.split(":")
    sensor_coordinates = sensor.replace("Sensor at x=", "").replace(" y=", "")
    beacon_coordinates = beacon.replace(" closest beacon is at x=", "").replace(" y=", "")
    sensor_coordinates = (int(sensor_coordinates.split(",")[0]), int(sensor_coordinates.split(",")[1]))
    beacon_coordinates = (int(beacon_coordinates.split(",")[0]), int(beacon_coordinates.split(",")[1]))

    if beacon_coordinates[1] == check_row:
      beacons_on_row.append(beacon_coordinates[0])

    x_distance = abs(beacon_coordinates[0] - sensor_coordinates[0])
    y_distance = abs(beacon_coordinates[1] - sensor_coordinates[1])
    total_distance = x_distance + y_distance

    if sensor_coordinates[1] + total_distance >= check_row and sensor_coordinates[1] - total_distance <= check_row:
      if sensor_coordinates[1] <= check_row:
        top = (sensor_coordinates[0], sensor_coordinates[1] + total_distance) 
      else:
        top = (sensor_coordinates[0], sensor_coordinates[1] - total_distance) 
      
      if top[1] == check_row:
        inelegible_positions.append(top[0])

      else:
        distance_from_check_row = top[1] - check_row
        if distance_from_check_row > 0:
          left = (top[0] - distance_from_check_row, top[1] - distance_from_check_row)
          right = (top[0] + distance_from_check_row, top[1] - distance_from_check_row)
        else:
          left = (top[0] + distance_from_check_row, top[1] - distance_from_check_row)
          right = (top[0] - distance_from_check_row, top[1] - distance_from_check_row)

        for i in range(left[0], right[0] + 1):
          inelegible_positions.append((i))

  print(f"Row {check_row} Inelegible Locations: {len(set(inelegible_positions)) - len(set(beacons_on_row))}")        
  
  for row in input.split("\n"):
    print(row)
    sensor, beacon = row.split(":")
    sensor_coordinates = sensor.replace("Sensor at x=", "").replace(" y=", "")
    beacon_coordinates = beacon.replace(" closest beacon is at x=", "").replace(" y=", "")
    sensor_coordinates = (int(sensor_coordinates.split(",")[0]), int(sensor_coordinates.split(",")[1]))
    beacon_coordinates = (int(beacon_coordinates.split(",")[0]), int(beacon_coordinates.split(",")[1]))

    x_distance = abs(beacon_coordinates[0] - sensor_coordinates[0])
    y_distance = abs(beacon_coordinates[1] - sensor_coordinates[1])
    total_distance = x_distance + y_distance

    left = (sensor_coordinates[0] - total_distance, sensor_coordinates[1])
    right = (sensor_coordinates[0] + total_distance, sensor_coordinates[1])
    if left[0] < 0:
      left = (0, left[1])
    elif left[0] > search_size:
      left = (search_size, left[1])

    if left[1] >= 0 and left[1] <= search_size:
      beacon_map[left[1]].append((left[0], right[0]))
    
    top = (sensor_coordinates[0], sensor_coordinates[1] - total_distance)

    for i in range(top[1], sensor_coordinates[1]):
      if i >= 0 and i < search_size + 1:
        distance = top[1] - i
        if distance > 0:
          left = (top[0] - distance, top[1] - distance)
          right = (top[0] + distance, top[1] - distance)
        else:
          left = (top[0] + distance, top[1] - distance)
          right = (top[0] - distance, top[1] - distance)

        if left[0] < 0:
          left = (0, left[1])
        if right[0] > search_size:
          right = (search_size, left[1])

        beacon_map[i].append((left[0], right[0]))

    bottom = (sensor_coordinates[0], sensor_coordinates[1] + total_distance)

    for i in range(sensor_coordinates[1] + 1, bottom[1] + 1):
      if i >= 0 and i < search_size + 1:
        distance = bottom[1] - i 
        
        if distance > 0:
          left = (bottom[0] - distance, bottom[1] - distance)
          right = (bottom[0] + distance, bottom[1] - distance)
        else:
          left = (bottom[0] + distance, bottom[1] - distance)
          right = (bottom[0] - distance, bottom[1] - distance)
 
        if left[0] < 0:
          left = (0, left[1])
        if right[0] > search_size:
          right = (search_size, left[1])
      
        beacon_map[i].append((left[0], right[0]))

  beacon_location = None
  for key, value in beacon_map.items():
    row = sorted(value)
    largest_value = row[0][1]
    for i in range(len(row) - 1):
      a, b = row[i], row[i + 1]
      if b[0] - a[1] == 2 and b[0] > largest_value:
        beacon_location = (b[0] - 1, key)
        print(f"Beacon Found: {beacon_location}, Tuning Frequency: {(beacon_location[0] * 4000000) + beacon_location[1]}")
        break
      if b[1] > largest_value:
        largest_value = b[1]        
    if beacon_location:
      break    

if __name__ == "__main__":
  solve()