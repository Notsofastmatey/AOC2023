#Determine the number of ways you could beat the record in each race. What do you get if you multiply these numbers together?

from functools import reduce
import operator

debug=False
input_data=[]
#Get the file
if debug:
  with open("sample6.txt") as file:
    for line in file:
      input_data.append(line.strip()) 
  #print(input_data)
else:
  with open("day6.txt") as file:
    for line in file:
      input_data.append(line.strip()) 
  #print(input_data)

def part1(input_data):
  #Clean the data
  times=[]
  distances=[]
  data = input_data[0]
  data = data.split(" ")
  for time in data:
    if time.isdigit():
      times.append(int(time.strip()))
    else:
      times.append(time.strip())
  while("" in times):
    times.remove("")
  times.pop(0)
  #print(times)

  data = input_data[1]
  data = data.split(" ")
  for distance in data:
    if distance.isdigit():
      distances.append(int(distance.strip()))
    else:
      distances.append(distance.strip())
  while("" in distances):
    distances.remove("")
  distances.pop(0)
  #print(distances)
  
  #Now find ways to win
  winners_list=[]
  for i,time in enumerate(times):
    winners=0
    t=time
    d=distances[i]
    print(f"Time is {t}")
    print(f"Current distance record is {d}")
    for held_time in range(0,t):
      speed = held_time
      travel_time = t-held_time
      distance = travel_time * speed
      winner = False
      if distance > d:
        winner=True
        winners +=1
      print(f"Speed: {speed}   Travel time: {travel_time}   Distance: {distance}   Winner: {winner}")
    winners_list.append(winners)
  print(winners_list)
  #Multiply the ways of winning together
  res = reduce(operator.mul, winners_list)
  return res

def part2():
  times=[40709879]
  distances=[215105121471005]
  winners_list=[]
  #Now find ways to win
  for i,time in enumerate(times):
    winners=0
    t=time
    d=distances[i]
    #print(f"Time is {t}")
    #print(f"Current distance record is {d}")
    for held_time in range(0,t):
      speed = held_time
      travel_time = t-held_time
      distance = travel_time * speed
      winner = False
      if distance > d:
        winner=True
        winners +=1
      #print(f"Speed: {speed}   Travel time: {travel_time}   Distance: {distance}   Winner: {winner}")
    winners_list.append(winners)
  print(winners_list)
  res=winners_list[0]
  return res

#Part1
#print(f"Part 1: {part1(input_data)}")

#Part2
print(f"Part 2: {part2()}")
