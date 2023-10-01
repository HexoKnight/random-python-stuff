from getch import getch
from random import choice

def calcmoves(current=[None for _ in range(9)], player=True, turn=True, alpha=None):
  new = {}
  points = -20 if player == turn else 20
  for i in range(0, 9):
    if current[i] == None:
      newboard = [turn if i == x else current[x] for x in range(9)]

      if (type(winner := newboard[0]) == bool and winner == newboard[1] == newboard[2]) or (type(winner := newboard[3]) == bool and winner == newboard[4] == newboard[5]) or (type(winner := newboard[6]) == bool and winner == newboard[7] == newboard[8]) or (type(winner := newboard[0]) == bool and winner == newboard[3] == newboard[6]) or (type(winner := newboard[1]) == bool and winner == newboard[4] == newboard[7]) or (type(winner := newboard[2]) == bool and winner == newboard[5] == newboard[8]) or (type(winner := newboard[0]) == bool and winner == newboard[4] == newboard[8]) or (type(winner := newboard[2]) == bool and winner == newboard[4] == newboard[6]):
        new[i] = winner
        points = (max if player == turn else min)(points, 1 if winner == player else -1)
        if alpha != None and ((player == turn and points >= alpha) or (player != turn and points < alpha)): return None
      elif len([_ for _ in newboard if _ == None]) == 0:
        new[i] = None
        points = (max if player == turn else min)(points, 0)
        if alpha != None and ((player == turn and points >= alpha) or (player != turn and points < alpha)): return None
      else:
        new[i] = calcmoves(newboard, player, not turn, alpha)
        if new[i] != None:
          points = (max if player == turn else min)(points, new[i]["points"])
          if alpha == None: alpha == points
          elif (player == turn and points >= alpha) or (player != turn and points < alpha): return None
  new["points"] = points
  return new

allmoves = calcmoves(player=False)

while True:
  current = allmoves.copy()
  board = [None for _ in range(9)]

  turn = False
  turns = 0
  win = None
  while True:
    turn = not turn
    if turns > 0: print("\033[5F", end="")
    for i in range(9):
      print(("  " if i%3 == 0 else " │ ") + (str(i+1) if board[i] == None else ("\033[96mX\033[m" if board[i] else "\033[93mO\033[m")) + ("\n ───┼───┼───\n" if (i%3 == 2 and i < 8) else ""), end="")
    #for move2 in range(9):
    #  print()
    #  if move2 in current:
    #    for move in range(9):
    #      if move in current[move2]: print((str(move+1) + ":" + str(current[move2][move]["points"] if type(current[move2][move]) == dict else current[move2][move])).ljust(10), end="")
    #      else: print(" "*10, end="")
    #print("\n")
    #for move in range(9):
    #  if move in current: print((str(move+1) + ":" + str(current[move]["points"] if type(current[move]) == dict else current[move])).ljust(10), end="")
    #  else: print(" "*10, end="")
    print("\n" + ("\033[96mX" if turn else "\033[93mO") + "\033[m: ", end="")
    if (type(winner := board[0]) == bool and winner == board[1] == board[2]) or (type(winner := board[3]) == bool and winner == board[4] == board[5]) or (type(winner := board[6]) == bool and winner == board[7] == board[8]) or (type(winner := board[0]) == bool and winner == board[3] == board[6]) or (type(winner := board[1]) == bool and winner == board[4] == board[7]) or (type(winner := board[2]) == bool and winner == board[5] == board[8]) or (type(winner := board[0]) == bool and winner == board[4] == board[8]) or (type(winner := board[2]) == bool and winner == board[4] == board[6]):
      win = winner
      break
    if turns > 8: break
    stringnum = ""
    if turn:
      while not stringnum.isdigit() or (num := int(stringnum)) == 0 or board[num-1] != None: stringnum = getch()
      current = current[num-1]
      board[num-1] = turn
    else:
      points = -20
      num = None
      draw = []
      for i in current:
        if i != "points":
          if current[i] == (not turn): continue
          elif current[i] == turn:
            num = [i]
            break
          elif current[i] == None:
            draw.append(i)
          elif current[i]["points"] > points:# and not (not turn) in current[i].values():
            points = current[i]["points"]
            num = [i]
          elif current[i]["points"] == points:
            num.append(i)
      acchoice = choice(draw) if num == None else choice(num)
      current = current[acchoice]
      board[acchoice] = turn
    turns += 1

  print("\r" + ((("\033[96mX\033[m" if win else "\033[93mO\033[m") + " wins") if type(win) == bool else "Draw") + "\n")