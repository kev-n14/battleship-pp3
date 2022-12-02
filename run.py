import random
scores = {"computer": 0 , "player" :0}
#CONSTANT VARIABLES
USER_BOARD = [[" "] *8 for i in range(8)]
USER_MOVE_BOARD = [[" "] *8 for i in range(8)]

PC_BOARD = [[" "] *8 for i in range(8)]
PC_MOVE_BOARD = [[" "] *8 for i in range(8)]
LENGTH_OF_SHIPS = [2,3]  
LETTERS_TO_NUM = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}




def print_board(board):
    print(" ","-"*16)
    print(' |A|B|C|D|E|F|G|H|')
    print(" ", "-"*16)
    
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
    print(" ")

def location_ships(board):
    for ship_size in LENGTH_OF_SHIPS:
        while True:
            if board == PC_BOARD:
                postion, row ,column = random.choice(["H", "V"]), random.randint(0,7),random.randint(0,7)

                if does_ship_fit(ship_size, row,column,postion):
                    if ship_extends_limit(board,row,column,postion,ship_size)== False:

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

                if does_ship_fit(ship_size, row, column, postion):

                    if ship_extends_limit(board, row, column, postion, ship_size) == False:

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
                postion = input("Please Enter Positon of ship Horizontal or Vertical (H or V): ").upper()
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
                print('Enter a valid number between 1-8')
        while True:
            try:
                column = input("Enter the letter column of the ship: ").upper()
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
                print('Enter a valid number between 1-8')
        while True:
            try:
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGH':
                    column = LETTERS_TO_NUM[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
        return row, column 
    









def does_ship_fit(LENGTH_OF_SHIPS, row , column, postion):
    if postion == "H":
        if column + LENGTH_OF_SHIPS > 8:
            return False
        else:
            return True
    else:
        if row + LENGTH_OF_SHIPS > 8:
            return False
        else:
            return True


def ship_extends_limit(board, row, column, postion, ship_size):
    if postion == "H":
        for i in range(column, column + ship_size):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + ship_size):
            if board[i][column] == "X":
                return True
    return False

def hit_counter(board):
    count = 0
    for row in board:
        for column in row:
            if column =="X":
                count +=1
    return count   

def determine_if_user_pc(board):
    if board == USER_MOVE_BOARD:
        user_board = board
        row, column = user_input(USER_MOVE_BOARD)
        return user_board, row, column
    
    elif board == PC_MOVE_BOARD:
        pc_board = board
        row, column = random.randint(0, 7), random.randint(0, 7)
        return pc_board, row, column



def move(board):
    #current_board,row, column1 = determine_if_user_pc(board)
    if board == USER_MOVE_BOARD:
        row, column = user_input(USER_MOVE_BOARD)
        if board[row][column] == "-":
            move(board)
        elif board[row][column] == "X":
            move(board)
            print("\n****** THAT WAS A HIT *******\n")
        elif PC_BOARD [row][column] == "X":
            board[row][column] = "X"
        
        else: 
            board[row][column] = "-"
            print("\n****** You MISSED *******\n")
            
        
    elif board == PC_MOVE_BOARD:
        row, column = random.randint(0, 7), random.randint(0, 7)
        if board[row][column] == "-":
            move(board)
        elif board[row][column] == "X":
            move(board)
        elif USER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"
            print("\n****** The Computer MISSED *******\n")
    else:
        print("Something went wrong")




def game():
    """

    """
    print("-"*70)
    print("  ____       _______ _______ _      ______  _____ _    _ _____ _____  ")
    print(" |  _ \   /\|__   __|__   __| |    |  ____|/ ____| |  | |_   _|  __ \ ")
    print(" | |_) | /  \  | |     | |  | |    | |__  | (___ | |__| | | | | |__) |")
    print(" |  _ < / /\ \ | |     | |  | |    |  __|  \___ \|  __  | | | |  ___/ ")
    print(" | |_) / ____ \| |     | |  | |____| |____ ____) | |  | |_| |_| |   ")
    print(" |____/_/    \_\_|     |_|  |______|______|_____/|_|  |_|_____|_|")
    print(" ")
    print("-"*70)
    
    location_ships(PC_BOARD)
    print_board(USER_BOARD)
    print_board(PC_BOARD)
    location_ships(USER_BOARD)

    while True:
        while True:
            print("\n -- Player Turn --\n")
            print("Guess enemy location\n")
            print_board(USER_MOVE_BOARD)
            move(USER_MOVE_BOARD)
            break
        if hit_counter(USER_MOVE_BOARD) == 5:
            print("*"*10, " YOU ARE THE WINNER " ,"*"*10)
            break


        while True:
            print("\n-- Computer Turn --\n")
            move(PC_MOVE_BOARD)
            break
        print_board(PC_MOVE_BOARD)
        if hit_counter(PC_MOVE_BOARD) == 5:
            print("*"*10, " THE COMPUTER WIN'S ","*"*10)
            break

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
    
        

