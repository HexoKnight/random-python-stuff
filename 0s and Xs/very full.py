def displayboard(board):
  print(f"  {board[0][0]} │ {board[0][1]} │ {board[0][2]}")
  print(" ───┼───┼───")
  print(f"  {board[1][0]} │ {board[1][1]} │ {board[1][2]}")
  print(" ───┼───┼───")
  print(f"  {board[2][0]} │ {board[2][1]} │ {board[2][2]}")

def check_win(board, player):
  if player == board[0][0] == board[0][1] == board[0][2] or player == board[1][0] == board[1][1] == board[1][2] or player == board[2][0] == board[2][1] == board[2][2] or player == board[0][0] == board[1][0] == board[2][0] or player == board[0][1] == board[1][1] == board[2][1] or player == board[0][2] == board[1][2] == board[2][2] or player == board[0][0] == board[1][1] == board[2][2] or player == board[0][2] == board[1][1] == board[2][0]:
    return True

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

print("X first, number 1 to 9")

turn = False
turns = 0
while not (check_win(board, "X") or check_win(board, "O") or turns == 9):
  turn = not turn
  turns += 1
  displayboard(board)
  num = int(input("1-9: "))-1
  board[num//3][num%3] = "X" if turn else "O"

if check_win(board, "X"): print("X wins!")
elif check_win(board, "O"): print("O wins!")
elif turns == 9: print("draw")