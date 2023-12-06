#Which of the numbers in the second section appear in the list of winning numbers? The first match makes the card worth one point and each match after the first doubles the point value of that card.
debug=False
scratchcards=[]
points=0

#Get the file
if debug:
  with open("sample4.txt") as file:
    for line in file:
      scratchcards.append(line.strip()) 
  #print(scratchcards)
else:
  with open("day4.txt") as file:
    for line in file:
      scratchcards.append(line.strip()) 
  #print(scratchcards)

def part1(scratchcards):
  total_points = 0
  for card in scratchcards:
    points=0
    winning_cards = 0
    #Remove everything before the :
    cardnum = card.split(":")[0].strip().split(" ")[1]
    print(cardnum)
    card = card.split(":")[1].strip()
    winners=card.split(" | ")[0].split(" ")
    winners[:] = [x for x in winners if x] 
    #List comprehension to remove empty strings (Empty strings evaluate to false. Slice assignment using the semi colon modifies the list in place.)
    owned = card.split(" | ")[1].split(" ")
    owned[:] = [x for x in owned if x]
    print(f"Winning cards: {winners}")
    print(f"Owned cards: {owned}")
    for card in owned:
      if card in winners:
        if points == 0:
          points = 1
        winning_cards +=1
    points = points * 2 **(winning_cards-1)
    print(f"Winning cards: {winning_cards}")
    print(f"Points: {points}")
    total_points += points
  return total_points

def part2(scratchcards):
  total_scratchcards = 0
  card_scores = []
  for card in scratchcards:
    winning_cards = 0
    #Remove everything before the :
    print("Hi")
    cardnum = card.split(":")[0].strip().split(" ")[-1]
    print(cardnum)
    card = card.split(":")[1].strip()
    winners=card.split(" | ")[0].split(" ")
    winners[:] = [x for x in winners if x] 
    #List comprehension to remove empty strings (Empty strings evaluate to false. Slice assignment using the semi colon modifies the list in place.)
    owned = card.split(" | ")[1].split(" ")
    owned[:] = [x for x in owned if x]
    for card in owned:
      if card in winners:
        winning_cards +=1
    print(f"Winning cards: {winning_cards}")
    card_scores.append([int(cardnum),winning_cards,1])
  print("Cardnum, Matches, Count")
  for card in card_scores:
    print(card)

  for i,c in enumerate(card_scores):
    if c[1]>0:
      starting_card=c[0]+1
      finishing_card = c[0]+c[1]
      for num in range(starting_card, finishing_card+1):
        print(num)
        num_copies = c[2]
        print(f"Number of copies: {num_copies}")
        card_scores[num-1][2] = card_scores[num-1][2]+(1 * num_copies)
        print(f"Adding {(1)} to card number {num} for a total of {card_scores[num-1][2]}")
        #The line above is close, but not quite right
  for card in card_scores:
    print(card)
    total_scratchcards += card[2]
  
  return total_scratchcards

#Part1
#print(f"Part 1: {part1(scratchcards)}")

#Part2
print(f"Part 2: {part2(scratchcards)}")
