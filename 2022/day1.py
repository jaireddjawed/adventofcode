elfCalorieTotals = []
currentElfCalAmt = 0

while True:
  snackCalorieAmt = input()

  if snackCalorieAmt == '':
    elfCalorieTotals.append(currentElfCalAmt)
    currentElfCalAmt = 0
  elif snackCalorieAmt == 'done':
    elfCalorieTotals.append(currentElfCalAmt)
    break
  else:
    currentElfCalAmt += int(snackCalorieAmt)

# Part 1 (Elf with most cals)
print(max(elfCalorieTotals))

# Part 2 (Top 3 elves with most cals)
elfCalorieTotals = sorted(elfCalorieTotals, reverse=True)
print(sum(elfCalorieTotals[0:3]))
