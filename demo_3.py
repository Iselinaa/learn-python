import random
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

board = []
tries = 5
board_size = 5
ships = []
total_ships = 5

for x in range(0, board_size):
  board.append(["O"] * board_size)

def print_board(board):
  for row in board:
      output = " ".join(row)
      output = output.replace("X", f"{bcolors.FAIL}X{bcolors.ENDC}")
      output = output.replace("S", f"{bcolors.OKGREEN}S{bcolors.ENDC}")
      output = output.replace("O", f"{bcolors.OKCYAN}O{bcolors.ENDC}")
      output = output.replace("H", f"{bcolors.WARNING}H{bcolors.ENDC}")
      print(output)
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
    break
# print(ships)

while tries > 0:
    guess_row = int(input("Guess Row: ")) - 1
    guess_col = int(input("Guess Col: ")) - 1

    if guess_row < 0 or guess_row > len(board) - 1 or guess_col < 0 or guess_col > len(board) - 1:
        print("Wrong coordinates!")
        continue

    hit_ship = False
    for ship in ships:
      if ship[0] == guess_row and ship[1] == guess_col:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Congratulations! You sank my battleship!")
        board[guess_row][guess_col] = 'H'
        print_board(board)
        hit_ship = True
        break
    if not hit_ship:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("You missed my battleship!")
      board[guess_row][guess_col] = 'X'
      tries -= 1
      print('You have ' + str(tries) + ' left!')
      print_board(board)   

if tries == 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('You lost!' )
    for ship in ships:
      board[ship[0]][ship[1]] = 'S'
    print_board(board)