from getkey import getkey
from os import system

board = [None for _ in range(9)]

turn = False
turns = 0
win = None
while True:
  turn = not turn
  system("clear")
  for i in range(9):
    print(("  " if i%3 == 0 else " │ ") + (str(i+1) if board[i] == None else ("\033[96mX\033[m" if board[i] else "\033[93mO\033[m")) + ("\n ───┼───┼───\n" if (i%3 == 2 and i < 8) else ""), end="")
  print("\n" + ("\033[96mX" if turn else "\033[93mO") + "\033[m: ", end="")
  if (type(winner := board[0]) == bool and winner == board[1] == board[2]) or (type(winner := board[3]) == bool and winner == board[4] == board[5]) or (type(winner := board[6]) == bool and winner == board[7] == board[8]) or (type(winner := board[0]) == bool and winner == board[3] == board[6]) or (type(winner := board[1]) == bool and winner == board[4] == board[7]) or (type(winner := board[2]) == bool and winner == board[5] == board[8]) or (type(winner := board[0]) == bool and winner == board[4] == board[8]) or (type(winner := board[2]) == bool and winner == board[4] == board[6]):
    win = winner
    break
  if turns > 8: break
  stringnum = ""
  while not stringnum.isdigit() or (num := int(stringnum)) == 0 or board[num-1] != None: stringnum = getkey()
  print(num)
  board[num-1] = turn
  turns += 1

if type(win) == bool: print(f"{'X' if win else 'O'} wins")
else: print("Draw")