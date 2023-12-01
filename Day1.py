#On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
#What is the sum of all of the calibration values?
debug=False

calib_values = [] #original list
correct_calib_values = [] # corrected list

#Get the file
if debug:
  with open("sample1.txt") as file:
    for line in file:
      calib_values.append(line.strip()) 
  #print(calib_values)
else:
  with open("day1.txt") as file:
    for line in file:
      calib_values.append(line.strip()) 
  #print(calib_values)

def extract(calib_values):
  correct_calib_value=""
  for value in calib_values:
    for c in value:
      if c.isdigit():
        #print(f"First: {c}")
        correct_calib_value = c
        break
    for c in reversed(value):
      if c.isdigit():
        #print(f"Second: {c}")
        correct_calib_value += c
        break
    #print(correct_calib_value)
    correct_calib_values.append(int(correct_calib_value))
  
  return sum(correct_calib_values)

def convertnumberstodigits(str):
  #print(str)
  newString=str
  #print(f"String length: {len(str)}")
  #print("First pass")
  for i in range(len(str)):
    substring = str[:i]
    #print(substring)
    if substring.isdigit():
      break
    elif "one" in substring:
      newString = str.replace("one", "1")
      break
    elif "two" in substring:
      newString = str.replace("two", "2")
      break
    elif "three" in substring:
      newString = str.replace("three", "3")
      break
    elif "four" in substring:
      newString = str.replace("four", "4")
      break
    elif "five" in substring:
      newString = str.replace("five", "5")
      break
    elif "six" in substring:
      newString = str.replace("six", "6")
      break
    elif "seven" in substring:
      newString = str.replace("seven", "7")
      break
    elif "eight" in substring:
      newString = str.replace("eight", "8")
      break
    elif "nine" in substring:
      newString = str.replace("nine", "9")
      break
    
  
  for i in range(len(str)-1,0,-1):
      substring = newString[i:]
      #print(substring)
      if substring.isdigit():
        break
      elif "one" in substring:
        newString = newString.replace("one", "1")
        break
      elif "two" in substring:
        newString = newString.replace("two", "2")
        break
      elif "three" in substring:
        newString = newString.replace("three", "3")
        break
      elif "four" in substring:
        newString = newString.replace("four", "4")
        break
      elif "five" in substring:
        newString = newString.replace("five", "5")
        break
      elif "six" in substring:
        newString = newString.replace("six", "6")
        break
      elif "seven" in substring:
        newString = newString.replace("seven", "7")
        break
      elif "eight" in substring:
        newString = newString.replace("eight", "8")
        break
      elif "nine" in substring:
        newString = newString.replace("nine", "9")
        break
  #print(newString)
  return newString

#Part1
#print(f"Part 1: {extract(calib_values)}")

#Part2

#Convert all strings to digits
final_calib_values = []
for value in calib_values:
  newValue = convertnumberstodigits(value)
  final_calib_values.append(newValue)
#print(final_calib_values)

#Run the part1 code again
print(f"Part 2: {extract(final_calib_values)}")

###Note: For some reason, having both functions (part one and two) uncommented causes one to fail. They both work independently!###
