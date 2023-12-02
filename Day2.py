#Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
debug=False
games=[]

#Get the file
if debug:
  with open("sample2.txt") as file:
    for line in file:
      games.append(line.strip().split(";")) 
  #print(games)
else:
  with open("day2.txt") as file:
    for line in file:
      games.append(line.strip().split(";")) 
  #print(games)

def part1(games):
  total=0
  for game in games:
    valid_game = True
    #Get the id
    id = game[0].split(": ")[0].replace("Game ","")
    print(id)
    #Now remove everything before the semi-colon
    game[0] = game[0].split(": ")[1]
    #Extract each draw
    for draw in game:
      draw=str(draw).lstrip()
      print(f"Draw: {draw}")
      #Split into colours
      colours = draw.split(", ")
      #Split into number and colour
      for colour in colours:
        num = colour.split(" ")[0]
        col = colour.split(" ")[1]
        print(num + col)
        if col == "red" and int(num) > 12:
          valid_game = False
        elif col == "green" and int(num) > 13:
          valid_game = False
        elif col == "blue" and int(num) > 14:
          valid_game = False
    if  valid_game: 
      total += int(id)
      print(f"This is a valid game: {id}")
  return total

def part2(games):
  total=0
  for game in games:
    min_red=0
    min_green=0
    min_blue=0
    #Now remove everything before the semi-colon
    game[0] = game[0].split(": ")[1]
    #Extract each draw
    for draw in game:
      draw=str(draw).lstrip()
      print(f"Draw: {draw}")
      #Split into colours
      colours = draw.split(", ")
      #Split into number and colour
      for colour in colours:
        num = colour.split(" ")[0]
        col = colour.split(" ")[1]
        #print(num + col)
        if col == "red" and int(num) > min_red:
          min_red = int(num)
        elif col == "green" and int(num) > min_green:
          min_green = int(num)
        elif col == "blue" and int(num) > min_blue:
          min_blue = int(num)
    game_power = min_red * min_green * min_blue
    print(f"Game power: {game_power}")
    total += game_power
  return total

#Part1
#print(f"Part 1: {part1(games)}")

#Part2
print(f"Part 2: {part2(games)}")
