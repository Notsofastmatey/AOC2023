#Any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. What is the sum of all of the part numbers in the engine schematic?
debug=True
schematic=[]
numbers=["0","1","2","3","4","5","6","7","8","9","."]

#Get the file
if debug:
  with open("sample3.txt") as file:
    for line in file:
      schematic.append(line.strip()) 
  print(schematic)
else:
  with open("day3.txt") as file:
    for line in file:
      schematic.append(line.strip()) 
  #print(schematic)

def part1(schematic):
  maxrows = len(schematic)-1
  partnums=[]
  total=0
  valid = False
  try: 
    for row, line in enumerate(schematic):
      maxcols= len(line)-1
      partnum=""
      for col, part in enumerate(line):  
        #Find parts
        if part.isdigit():
          partnum += part
          #print(partnum)
          #print(f"Row {row}")
          #print(f"Column: {col}")
          #Check if adjacent to a symbol
          if col > 0:
            if schematic[row][col-1] not in numbers:
              #print(f"Found: {schematic[row][col-1]}")
              valid=True
          if row > 0 and col > 0:
            if schematic[row-1][col-1] not in numbers:
              #print(f"Found: {schematic[row-1][col-1]}")
              valid=True
          if row > 0:
            if schematic[row-1][col] not in numbers:
              #print(f"Found: {schematic[row-1][col]}")
              valid=True
          if row > 0 and col < maxcols:
            if schematic[row-1][col+1] not in numbers:
              #print(f"Found: {schematic[row-1][col+1]}")
              valid=True
          if col < maxcols:
            if schematic[row][col+1] not in numbers:
              #print(f"Found: {schematic[row][col+1]}")
              valid=True
          if row <maxrows and col < maxcols:
            if schematic[row+1][col+1] not in numbers:
              #print(f"Found: {schematic[row+1][col+1]}")
              valid=True
          if row < maxrows:
            if schematic[row+1][col] not in numbers:
              #print(f"Found: {schematic[row+1][col]}")
              valid=True
          if row < maxrows and col > 0: 
            if schematic[row+1][col-1] not in numbers:
              #print(f"Found: {schematic[row+1][col-1]}")
              valid=True
          #print(f"Valid: {valid}")
        #Else it's the end of the part number so store it
        if not part.isdigit() or col == maxcols:
          #print(partnum)
          
          if valid: 
            partnum = partnum.strip()
            partnums.append(int(partnum))
            
          partnum=""
          valid= False
  except IndexError:
    print("Out of range")
  #print("End of schematic")
  return sum(partnums)

def part2(schematic):
  gear_schematic = schematic.copy()
  asterisks = []
  partnum_locations=[]
  maxrows = len(schematic)-1
  partnums=[]
  valid = False
  try: 
    for row, line in enumerate(schematic):
      maxcols= len(line)-1
      partnum=""
      for col, part in enumerate(line):  
        #Find parts
        
        if part.isdigit():
          partnum += part
          print(partnum)
          print(f"Row {row}")
          print(f"Column: {col}")
          #Check if adjacent to a symbol
          if col > 0:
            if schematic[row][col-1] not in numbers:
              print(f"Found: {schematic[row][col-1]}")
              valid=True
          if row > 0 and col > 0:
            if schematic[row-1][col-1] not in numbers:
              print(f"Found: {schematic[row-1][col-1]}")
              valid=True
          if row > 0:
            if schematic[row-1][col] not in numbers:
              print(f"Found: {schematic[row-1][col]}")
              valid=True
          if row > 0 and col < maxcols:
            if schematic[row-1][col+1] not in numbers:
              print(f"Found: {schematic[row-1][col+1]}")
              valid=True
          if col < maxcols:
            if schematic[row][col+1] not in numbers:
              print(f"Found: {schematic[row][col+1]}")
              valid=True
          if row <maxrows and col < maxcols:
            if schematic[row+1][col+1] not in numbers:
              print(f"Found: {schematic[row+1][col+1]}")
              valid=True
          if row < maxrows:
            if schematic[row+1][col] not in numbers:
              print(f"Found: {schematic[row+1][col]}")
              valid=True
          if row < maxrows and col > 0: 
            if schematic[row+1][col-1] not in numbers:
              print(f"Found: {schematic[row+1][col-1]}")
              valid=True
          print(f"Valid: {valid}")
        #Else it's the end of the part number so store it
        if not part.isdigit() or col == maxcols:
          print(partnum)
  
          if valid: 
            partnum = partnum.strip()
            partnums.append(int(partnum))
            partnum_locations.append([partnum, row, col-1])
            #Now let's mark all the parts in the new schematic
            part_size = len(partnum)
            current_row = gear_schematic[row]
            print(f"The current row is: {current_row}")
            new_row = current_row[:col-(part_size)] + "G"*part_size + current_row[col:]
            print(f"The new row is: {new_row}")
            gear_schematic[row] = new_row
  
          partnum=""
          valid= False
  except IndexError:
    print("Out of range")
  print("End of schematic")
  for row in gear_schematic:
    print(row)
  
  
  #Now we look for the asterisks
  parts = 0
  try: 
    for row, line in enumerate(gear_schematic):
      maxcols= len(line)-1
      partnum=""
      for col, part in enumerate(line):  
        #Find asterisks

        if part =="*":
          #Check if adjacent to a part number
          if col > 0:
            if gear_schematic[row][col-1] == "G":
              print(f"Found: {schematic[row][col-1]}")
              parts+=1
          if row > 0 and col > 0:
            if gear_schematic[row-1][col-1] == "G":
              print(f"Found: {schematic[row-1][col-1]}")
              parts+=1
          if row > 0:
            if gear_schematic[row-1][col] == "G":
              print(f"Found: {schematic[row-1][col]}")
              parts+=1
          if row > 0 and col < maxcols:
            if gear_schematic[row-1][col+1] == "G":
              print(f"Found: {schematic[row-1][col+1]}")
              parts+=1
          if col < maxcols:
            if gear_schematic[row][col+1] == "G":
              print(f"Found: {schematic[row][col+1]}")
              parts+=1
          if row <maxrows and col < maxcols:
            if gear_schematic[row+1][col+1] == "G":
              print(f"Found: {schematic[row+1][col+1]}")
              parts+=1
          if row < maxrows:
            if gear_schematic[row+1][col] not in numbers:
              print(f"Found: {schematic[row+1][col]}")
              parts+=1
          if row < maxrows and col > 0: 
            if gear_schematic[row+1][col-1] == "G":
              print(f"Found: {schematic[row+1][col-1]}")
              parts+=1
          print(f"Valid: {valid}")
        #Else it's the end of the part number so store it
        #if not part.isdigit() or col == maxcols:
          #print(partnum)

          if parts>1: 
            #Log the location of the asterisk for now
            asterisks.append([row,col])
          parts=0
  except IndexError:
    print("Out of range")

  for ast in asterisks:
    print(ast)
  for row in partnum_locations:
    print(row)
  #So now all I have to do is compare the 2 lists (I think)
  for ast in asterisks:
    for part in partnum_locations:
      if ast[0] == part[1] or ast[0] == part[1]-1 or ast[0] == part[1]+1:
        if ast[1] == part[2] or ast[1] == part[1]-1 or ast[1] == part[1]+1:
          #This doesn't cope with partnumbers with more than one digit. Need to use their length. Also currently adds 633 to the first gear
          ast.append(part[0])
          print(asterisks)

#Part1
#print(f"Part 1: {part1(schematic)}")

#Part2
print(f"Part 2: {part2(schematic)}")
