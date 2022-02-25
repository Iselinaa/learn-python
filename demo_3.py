import random
import os

board = []
tries = 5
board_size = 10
ships = []
total_ships = 5

for x in range(0, board_size):
  board.append(["O"] * board_size)

def print_board(board):
  for row in board:
      print(" ".join(row))

print_board(board)

def random_row(board):
  return random.randint(0, len(board) - 1)

def random_col(board):
  return random.randint(0, len(board) - 1)

for s in range(0, total_ships):
  while True:
    ship_row = random_row(board)
    ship_col = random_col(board)
    found_ship_with_same_coordinates = False
    for coordinate in ships:
      if ship_row == coordinate[0] and ship_col == coordinate[1]:
        found_ship_with_same_coordinates = True
        break
    if found_ship_with_same_coordinates:
      continue
    ships.append([ship_row, ship_col])
# print(ships)

while tries > 0:
    guess_row = int(input("Guess Row: ")) - 1
    guess_col = int(input("Guess Col: ")) - 1

    if guess_row < 0 or guess_row > len(board) - 1 or guess_col < 0 or guess_col > len(board) - 1:
        print("Wrong coordinates!")
        continue

    # print(ship_row)
    # print(ship_col)

    # Write your code below!
    if guess_row == ship_row and guess_col == ship_col:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Congratulations! You sank my battleship!")
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You missed my battleship!")
        board[guess_row][guess_col] = 'X'
        tries -= 1
        print('You have ' + str(tries) + ' left!')
        print_board(board)
if tries == 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('You lost!' )
    board[ship_row][ship_col] = 'S'
    print_board(board)