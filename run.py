import random

# CONSTANT VARIABLES
USER_BOARD = [[" "] * 8 for i in range(8)]
USER_MOVE_BOARD = [[" "] * 8 for i in range(8)]
PC_BOARD = [[" "] * 8 for i in range(8)]
PC_MOVE_BOARD = [[" "] * 8 for i in range(8)]
NUMBER_OF_SHIPS = [2, 3, 3, 4, 5]
LETTERS_TO_NUM = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


def print_board(board):
    """
    To print board with A to H for the columns
    and row 1 to 8. For all boards passed in

    """
    print(" ", "-"* 16)
    print(' |A|B|C|D|E|F|G|H|')
    print(" ", "-"* 16)
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
    print(" ")


def location_ships(board, name):
    """

    """
    for ship_size in NUMBER_OF_SHIPS: # for loop to iterate through list of NUMBER_OF_SHIPS
        while True:
            if board == PC_BOARD: # when board passed is the PC board
                position, row, column = random.choice(
                    ["H", "V"]), random.randint(0, 7), random.randint(0, 7)# random assign values for orientation, row, column
                if does_ship_fit(ship_size, row, column, position): # passes values to function to determine if true
                    if overlapping(board, row, column, position, ship_size) is False: # 
                        if position == "H":
                            for i in range(column, column + ship_size):
                                board[row][i] = "O"
                        else:
                            for i in range(row, row + ship_size):
                                board[i][column] = "O"
                        break
            else:
                location_ship = True
                print('Place the ship with a length of ' + str(ship_size))# message to player about size of ship
                row, column, position = user_input(location_ship, name)# get values from player for row, column, orientation
                if does_ship_fit(ship_size, row, column, position):# passes values to function to determine if true
                    if overlapping(board, row, column, position, ship_size) is False: 
                        if position == "H":
                            for i in range(column, column + ship_size):
                                board[row][i] = "O"
                        else:
                            for i in range(row, row + ship_size):
                                board[i][column] = "O"
                        print_board(USER_BOARD)
                        break


def user_name():
    """
    Get Player name from user.
    """
    user_name = input("Please Enter Name: \n") # gets Players name
    return user_name # returns Players name


def user_input(location_ship, name):
    """
    To ask user orientation and position 
    of each ship.
    Ask user where to guess on computer board
    """
    if location_ship is True:
        while True:
            try:
                postion = input(f"{name}, Please Enter Positon of ship Horizontal or Vertical (H or V): \n").upper()
                if postion == "H" or postion == "V":
                    break
            except TypeError:
                print('Enter a valid postion H or V')
        while True:
            try:
                row = input("Enter the row 1-8 of the ship: \n")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid number between 1-8')
        while True:
            try:
                column = input("Enter the letter column of the ship: \n").upper()
                if column in 'ABCDEFGH':
                    column = LETTERS_TO_NUM[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
        return row, column, postion
    else:
        while True:
            try:
                row = input("Enter the row number (1-8) to attack : \n")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid number between 1-8')
        while True:
            try:
                column = input("Enter the column letter (A-H) to attack: \n").upper()
                if column in 'ABCDEFGH':
                    column = LETTERS_TO_NUM[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
        return row, column


def does_ship_fit(NUMBER_OF_SHIPS, row, column, postion):
    """
    Determine if the ship will fit on board by it's
    orientation, column letter and row number
    """
    if postion == "H":
        if column + NUMBER_OF_SHIPS > 8:  
            return False
        else:
            return True
    else:
        if row + NUMBER_OF_SHIPS > 8:
            return False
        else:
            return True


def overlapping(board, row, column, postion, ship_size):
    """
    To find out if the ship to be placed will overlap an existing ship
    already in place.
    """
    if postion == "H":
        for i in range(column, column + ship_size):
            if board[row][i] == "O":
                return True
    else:
        for i in range(row, row + ship_size):
            if board[i][column] == "O":
                return True
    return False


def hit_counter(board):
    """
    Count each X or hit on a board.
    return this number

    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


def move(board, name):
    """
    to determine if the coordinates from the player or computer has already 
    guessed if so tery again. if not, are these cordinates a  hit or miss. 

    """
    if board == USER_MOVE_BOARD: # when board is player move board
        row, column = user_input(USER_MOVE_BOARD, name) # call function to print out questions to player, assign row, column
        if board[row][column] == "-": # if coordinates passed have "-" assigned, then display message
            print("You already tried those coordinates. Try Again")
            move(board, name) # function calls itself so player can guess again
        elif board[row][column] == "X":# if coordinates passed have "X" assigned
            print("You already tried those coordinates. Try Again")
            move(board, name)# function calls itself so player can guess again
        elif PC_BOARD[row][column] == "O": # if coordinates on PC_Board are equal to "O"
            board[row][column] = "X" # then mark board with "X" for a hit, then display message
            print(f"\n****** THAT WAS A HIT {name} *******\n")

        else:
            board[row][column] = "-" # mark board with "-" for a miss,then display message
            print(f"\n****** You MISSED {name} *******\n")

    elif board == PC_MOVE_BOARD:
        row, column = random.randint(0, 7), random.randint(0, 7)# randomly assign values to row, column
        if board[row][column] == "-":# if coordinates passed have "-" assigned
            move(board, name)# function calls itself so computer can guess again
        elif board[row][column] == "X":# if coordinates passed have "X" assigned
            move(board, name)# function calls itself so computer can guess again
        elif USER_BOARD[row][column] == "O":# if coordinates on USER_BOARD are equal to "O"
            board[row][column] = "X"# then mark board with "X" for a hit, then display message
            print("***** The Computer Got A Hit ******")
        else:
            board[row][column] = "-" # mark board with "-" for a miss,then display message
            print("\n****** The Computer MISSED *******\n")


def game():
    """
    Starts a new game. Displays logo and calls functiions for user and computer to populate boards.
    Displays text and calls functions for each round.  
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
    name = user_name()# player name is assinged to name 
    location_ships(PC_BOARD, name)
    #print_board(PC_BOARD) # to display the computers board (for testing purposes) 
    print(f"{name}\'s Board")
    print_board(USER_BOARD) # players board  is printed
    location_ships(USER_BOARD, name)# called to allow the user to populate board
    round = 1 # value to count round
    while True:
        while True:
            print(f" ----- ROUND {round} -----")
            print(" ")
            hits_needed = sum(NUMBER_OF_SHIPS)
            print(f"{name} Score: {hit_counter(USER_MOVE_BOARD)}/{hits_needed} vs Computer Score: {hit_counter(PC_MOVE_BOARD)}/{hits_needed}")
            print(f"\n -- {name}'s Move --\n")
            print(f"{name}\'s Guess Board")
            print_board(USER_MOVE_BOARD)
            move(USER_MOVE_BOARD, name)
            print(f"{name} score: {hit_counter(USER_MOVE_BOARD)} ")
            round += 1
            break
        if hit_counter(USER_MOVE_BOARD) == 17:
            print("*"*10, f"{name} IS THE WINNER ", "*"*10)
            print("*"*10, f"Congratulations {name} ", "*"*10)
            break

        while True:
            print("\n-- Computer Turn --\n")
            print(f"Computer\'s Guess Board")
            move(PC_MOVE_BOARD, name)
            break
        print_board(PC_MOVE_BOARD)
        if hit_counter(PC_MOVE_BOARD) == 17:
            print("*"*10, " THE COMPUTER WIN'S ", "*"*10)
            print("*"*10, f" BETTER LUCK NEXT TIME {name} ", "*"*10)
            break


game()
