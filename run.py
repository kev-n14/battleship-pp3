import random
scores = {"computer": 0 , "player" :0}
#CONSTANT VARIABLES
USER_BOARD = [[" "] *8 for i in range(8)]
PC_BOARD = [[" "] *8 for i in range(8)]
LENGTH_OF_SHIPS = [2,3]  
LETERS_TO_NUM = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}




def print_board(board):
    return print(" A B C D E F G H")
    print(" ","-"*10)
    print(" ", "-"*16)
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def location_ships(board):
    for ship_size in LENGTH_OF_SHIPS:
        while True:
            if board == PC_BOARD:
                postion, row ,column = random.choice(["H", "V"]), random.randint(0,7),random.randint(0,7)

                #if does_ship_fit(ship_length, row,column,postion):
                    #if ship_extends_limit(board,row,column,postion,ship_size)== False:

                        if postion=="H":
                            for i in range(column,column + ship_size):
                                board[row][i] = "O"
                    else:
                        for i in range(row, row + ship_size):
                            board[i][column] = "O"
                    break
            else:
                place_ship = True
                print('Please place the ship with a length of ' + str(ship_size))
                row, column, postion = user_input(place_ship)

                #if does_ship_fit(ship_size, row, column, postion):

                    #if ship_extends_limit(board, row, column, postion, ship_size) == False:

                        if postion == "H":
                            for i in range(column, column + ship_size):
                                board[row][i] = "O"
                else:
                    for i in range(row, row + ship_size):
                        board[i][column] = "O"
                print_board(USER_BOARD)
                break

def user_input(place_ship):
    if place_ship == True:
        while True:
            try:
                postion = input("Please Enter Positon of ship Horizontal or Vertical(H or V): ").upper()
                if postion == "H" or postion == "V":
                    break
            except TypeError:
                print('Enter a valid postion H or V')
        while True:
            try:
                row = input("Enter the row 1-8 of the ship: ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid letter between 1-8')
        while True:
            try:
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGH':
                    column = LETTERS_TO_NUM[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
        return row, column, postion
    else:
        while True:
            try:
                row = input("Enter the row 1-8 of the ship: ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid letter between 1-8')
        while True:
            try:
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGH':
                    column = LETTERS_TO_NUM[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
        return row, column 
    









#def does_ship_fit():
#def ship_extends_limit():

def game():
    """

    """
    size = 5
    num_ships = 4
    scores["computer"]=0
    scores["player"] = 0
    print("-"*40)
    print("      ***** BATTLESHIPS *****     ")
    print("-"*40)
    location_ships(PC_BOARD)
    print_board(USER_BOARD)
    location_ships(USER_BOARD)

    #size = 2
    #num_ships= 2
    #scores['COMPUTER'] = 0
    #scores['PLAYER'] = 0

    
    
    #print()
    
    #for col_num in range(1):
        #   print('  | A | B | C | D | E | F | G | H |')

        #  for row_num in range(1,9):
        #     print("  ","---"*11)
        #    print(row_num,"|",  "  | "*8)
        #print("%d|%s|" % (row_num, "|".join(row)))
        
    #print()
    #print('-'*40)
    #print(f"Board size: {size}. number of ships {num_ships}")
    #print("-"*40)
    #compBoard = Board(size, num_ships, 'computer', type = "COMPUTER")
    #playerBoard = Board(size, num_ships, user_name, type= "PLAYER") 


game()
    
        

