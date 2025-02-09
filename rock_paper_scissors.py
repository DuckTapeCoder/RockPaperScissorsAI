games = []
import random
valid = False
while not valid:
  try:
    total = int(input("How many games would you like to play?   "))
    if total >= 1:
      valid = True
  except ValueError:
    print("That is not a valid input. Please input a valid number")
rps = random.randint(1,3)
inp = input("Please select your choice.    R/P/S    ")
inp = inp.lower()
if inp == "r":
  inp = 1
if inp == "p":
  inp = 2
if inp == "s":
  inp = 3
if rps == 1:
  print("I picked Rock")
if rps == 2:
  print("I picked Paper")
if rps == 3:
  print("I picked Scissors")
if inp == rps:
  print("Tie")
  games.append("Tie")
elif inp == 1:
  if rps == 2:
    print("You Lose")
    games.append("Loss")
  elif rps == 3:
    print("You Win")
    games.append("Win")
elif inp == 2:
  if rps == 1:
    print("You Win")
    games.append("Win")
  elif rps == 3:
    print("You Lose")
    games.append("Loss")
elif inp == 3:
  if rps == 1:
    print("You Lose")
    games.append("Loss")
  elif rps == 2:
    print("You Win")
    games.append("Win")
else:
  print("You did not pick a viable option. You lose")
  games.append("Loss")
if total > 1:
  rps2 = random.randint(1,5)
  inp = input("Please select your choice.    R/P/S    ")
  if rps2 == 1:
    print("I picked Rock")
  if rps2 == 2:
   print("I picked Paper")
  if rps2 == 3:
    print("I picked Scissors")
  if rps == 1:
    if rps2 == 4:
      print("I picked Paper")
      rps2 = 2
    elif rps2 == 5:
     print("I picked Scissors")
     rps2 = 3
  elif rps == 2:
    if rps2 == 4:
      print("I picked Rock")
      rps2 = 1
    elif rps2 == 5:
      print("I picked Scissors")
      rps2 = 3
  elif rps == 3:
    if rps2 == 4:
      print("I picked Rock")
      rps2 = 1
    elif rps2 == 5:
      print("I picked Paper")
      rps2 = 2
  inp = inp.lower()
  if inp == "r":
    inp = 1
  if inp == "p":
    inp = 2
  if inp == "s":
    inp = 3
  if inp == rps2:
    print("Tie")
    games.append("Tie")
  elif inp == 1:
    if rps2 == 2:
      print("You Lose")
      games.append("Loss")
    elif rps2 == 3:
     print("You Win")
     games.append("Win")
  elif inp == 2:
    if rps2 == 1:
      print("You Win")
      games.append("Win")
    elif rps2 == 3:
      print("You Lose")
      games.append("Loss")
  elif inp == 3:
    if rps2 == 1:
      print("You Lose")
      games.append("Loss")
    elif rps2 == 2:
      print("You Win")
      games.append("Win")
  else:
    print("You did not pick a viable option. You lose")
    games.append("Loss")
count = 2
while count < total:
  rps3 = random.randint(1,6)
  inp = input("Please select your choice.    R/P/S    ")
  inp = inp.lower()
  if inp == "r":
    inp = 1
  if inp == "p":
    inp = 2
  if inp == "s":
    inp = 3
  if rps == rps2:
    if rps3 == 4:
      rps3 = 1
    if rps3 == 5:
      rps3 = 2
    if rps3 == 6:
      rps3 = 3
  elif rps == 1:
    if rps2 == 2:
      if rps3 == 4:
        rps3 = 1
      elif rps3 == 5:
        rps3 = 3
      elif rps3 == 6:
        rps3 = 3
    elif rps2 == 3:
      if rps3 == 4:
        rps3 = 1
      elif rps3 == 5:
        rps3 = 2
      elif rps3 == 6:
        rps3 = 2
  elif rps == 2:
    if rps2 == 1:
      if rps3 == 4:
        rps3 = 2
      elif rps3 == 5:
        rps3 = 3
      elif rps3 == 6:
        rps3 = 3
    elif rps2 == 3:
      if rps3 == 4:
        rps3 = 2
      elif rps3 == 5:
        rps3 = 1
      elif rps3 == 6:
        rps3 = 1
  elif rps == 3:
    if rps2 == 1:
      if rps3 == 4:
        rps3 = 3
      elif rps3 == 5:
        rps3 = 2
      elif rps3 == 6:
        rps3 = 2
    elif rps2 == 2:
      if rps3 == 4:
        rps3 == 3
      elif rps3 == 5:
        rps3 = 1
      elif rps3 == 6:
        rps3 = 1
  if rps3 == 1:
    print("I picked Rock")
  if rps3 == 2:
    print("I picked Paper")
  if rps3 == 3:
    print("I picked Scissors")
  if inp == rps2:
   print("Tie")
   games.append("Tie")
  elif inp == 1:
    if rps2 == 2:
      print("You Lose")
      games.append("Loss")
    elif rps2 == 3:
      print("You Win")
      games.append("Win")
  elif inp == 2:
    if rps2 == 1:
      print("You Win")
      games.append("Win")
    elif rps2 == 3:
     print("You Lose")
     games.append("Loss")
  elif inp == 3:
   if rps2 == 1:
    print("You Lose")
    games.append("Loss")
   elif rps2 == 2:
      print("You Win")
      games.append("Win")
  else:
    print("You did not pick a viable option. You lose")
    games.append("Loss")
  count = count + 1
  rps = rps2
  rps2 = rps3
print()
w = 0
l = 0
t = 0
count = 0
while count < total:
  print("Game " + str(count+1) + ": " + games[count])
  if games[count] == "Win":
    w = w + 1
  elif games[count] == "Loss":
    l = l + 1
  elif games[count] == "Tie":
    t = t + 1
  count += 1
w = str(w)
l = str(l)
t = str(t)
if t == "0":
  print(w + '-' + l)
else:
  print(w + '-' + l + '-' + t)


input()