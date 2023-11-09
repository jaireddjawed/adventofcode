elfChoices, playerChoices = [], []

while True:
  match = input()

  if match == 'done':
    break

  elfChoice, playerChoice = match.split(' ')
  elfChoices.append(elfChoice)
  playerChoices.append(playerChoice)

def partOne():
  myScore = 0

  for elfChoice, playerChoice in zip(elfChoices, playerChoices):
    if playerChoice == 'X':
      # represents rock, player score is incremented by 1 for choosing this
      myScore += 1
    elif playerChoice == 'Y':
      # paper, incremented by 2
      myScore += 2
    elif playerChoice == 'Z':
      myScore += 3

    # elf choice A -> rock, B -> paper, C -> scissors
    # draw match, both elf and player choose the same item
    if (elfChoice == 'A' and playerChoice == 'X') or (elfChoice == 'B' and playerChoice == 'Y') or (elfChoice == 'C' and playerChoice == 'Z'):
      myScore += 3

    # player loss
    if (elfChoice == 'A' and playerChoice == 'Z') or (elfChoice == 'B' and playerChoice == 'X') or (elfChoice == 'C' and playerChoice == 'Y'):
      myScore += 0

    # player win
    if (playerChoice == 'X' and elfChoice == 'C') or (playerChoice == 'Y' and elfChoice == 'A') or (playerChoice == 'Z' and elfChoice == 'B'):
      myScore += 6

  print(myScore)

def partTwo():
  myScore = 0

  for elfChoice, playerOutcome in zip(elfChoices, playerChoices):
    # ends in loss
    if playerOutcome == 'X':
      if elfChoice == 'A':
        # we pick scissors
        myScore += 3
      elif elfChoice == 'B':
        myScore += 1
      elif elfChoice == 'C':
        myScore += 2

    # ends in a draw
    if playerOutcome == 'Y':
      myScore += 3

      if elfChoice == 'A':
        myScore += 1
      elif elfChoice == 'B':
        myScore += 2
      elif elfChoice == 'C':
        myScore += 3

    # ends in player winning
    if playerOutcome == 'Z':
      myScore += 6

      if elfChoice == 'A':
        # paper needs to be chosen in response to the elf's rock
        myScore += 2
      elif elfChoice == 'B':
        myScore += 3
      elif elfChoice == 'C':
        myScore += 1

  print(myScore)

partOne()
partTwo()
