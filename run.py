import random

# CONSTANT VARIABLES
USER_BOARD = [[" "] * 8 for i in range(8)]  # grid 8 rows by 8 columns of blank spaces
USER_MOVE_BOARD = [[" "] * 8 for i in range(8)]
PC_BOARD = [[" "] * 8 for i in range(8)]
PC_MOVE_BOARD = [[" "] * 8 for i in range(8)]
NUMBER_OF_SHIPS = [2, 3, 3, 4, 5]  # list of ships, different size ships
LETTERS_TO_NUM = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}  # assign numbers to letters to be used in columns


def print_board(board):
    """
    To print board with A to H for the columns
    and row 1 to 8. For all boards passed in

    """
    print(" ", "-" * 16)
    print(' |A|B|C|D|E|F|G|H|')  # for column of board
    print(" ", "-" * 16)
    row_number = 1
    for row in board:  # iterate through to print row number and divider
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1  # row_number is incremented by 1
    print(" ")


def location_ships(board, name):
    """
    Place ships on the Player and Computer board.
    For the computer randomly select orientation, row,column.
    """
    for ship_size in NUMBER_OF_SHIPS:  # for loop to iterate through list of NUMBER_OF_SHIPS
        while True:
            if board == PC_BOARD:  # when board passed is the PC board
                position, row, column = random.choice(
                    ["H", "V"]), random.randint(0, 7), random.randint(0, 7)  # randomly assign values for orientation, row, column
                if does_ship_fit(ship_size, row, column, position):  # passes values to function to determine if true
                    if overlapping(board, row, column, position, ship_size) is False:
                        if position == "H":  # when ship placed horizontally and not overlaapping
                            for i in range(column, column + ship_size):
                                board[row][i] = "O"  # ship represented by "O" columns populated
                        else:
                            for i in range(row, row + ship_size):
                                board[i][column] = "O"  # ship represented by "O" rows populated
                        break
            else:
                location_ship = True
                print('Place the ship with a length of ' + str(ship_size))  # message to player about size of ship
                row, column, position = user_input(location_ship, name)  # get values from player for row, column, orientation
                if does_ship_fit(ship_size, row, column, position):  # passes values to function to determine if true
                    if overlapping(board, row, column, position, ship_size) is False:  # function to handle if ship overlaps, must return false
                        if position == "H":
                            for i in range(column, column + ship_size):
                                board[row][i] = "O"  # ship represented by "O" columns populated
                        else:
                            for i in range(row, row + ship_size):
                                board[i][column] = "O"  # ship represented by "O" rows populated
                        print_board(USER_BOARD)   # print board to show Player updated board
                        break


def user_name():
    """
     Get the Player name from the user.
    """
    user_name = input("Please Enter Name: \n")  # gets Players name
    return user_name  # returns Players name


def user_input(location_ship, name):
    """
    To ask about Player orientation and position
    of each ship.
    Ask the Player where to guess on the computer board
    """
    if location_ship is True:  # to populate board, user choose orientation, row and column
        while True:
            try:  # assigning orientation value to postion from Player
                postion = input(f"{name}, Please Enter Positon of ship Horizontal or Vertical (H or V): \n").upper()
                if postion == "H" or postion == "V":
                    break
            except TypeError:  # if incorrect value entered error caught and message is print
                print('Enter a valid postion H or V')
        while True:
            try:  # assigning row value to row from Player
                row = input("Enter the row 1-8 of the ship: \n")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:  # if incorrect value entered error caught and message is print
                print('Enter a valid number between 1-8')
        while True:
            try:  # assigning column value to column from Player
                column = input("Enter the letter column of the ship: \n").upper()
                if column in 'ABCDEFGH':
                    column = LETTERS_TO_NUM[column]
                    break
            except KeyError:  # if incorrect value entered error caught and message is print
                print('Enter a valid letter between A-H')
        return row, column, postion
    else:  # get input from player to choose which block to attck on computer board
        while True:
            try:
                row = input("Enter the row number (1-8) to attack : \n")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:  # if incorrect value entered error caught
                print('Enter a valid number between 1-8')
        while True:
            try:
                column = input("Enter the column letter (A-H) to attack: \n").upper()
                if column in 'ABCDEFGH':
                    column = LETTERS_TO_NUM[column]
                    break
            except KeyError:  # if incorrect value entered error caught
                print('Enter a valid letter between A-H')
        return row, column


def does_ship_fit(NUMBER_OF_SHIPS, row, column, postion):
    """
    Determine if the ship will fit on board by it's
    orientation, column letter, and row number
    """
    if postion == "H":
        if column + NUMBER_OF_SHIPS > 8:  # determine if column selcted + length of ships is less than height of board 8
            return False
        else:
            return True
    else:
        if row + NUMBER_OF_SHIPS > 8:  # determine if row selcted + length of ships is less than height of board 8
            return False
        else:
            return True


def overlapping(board, row, column, postion, ship_size):
    """
    To find out if the ship to be placed will overlap an existing ship
    already in place.
    """
    if postion == "H":
        for i in range(column, column + ship_size):  # iterate through to determine if a ship is present in columns
            if board[row][i] == "O":
                return True
    else:
        for i in range(row, row + ship_size):  # iterate through to determine if a ship is present in rows
            if board[i][column] == "O":
                return True
    return False


def hit_counter(board):
    """
    Count each X or hit on a board.
    return this number

    """
    count = 0
    for row in board:  # for loop iterate  through each row
        for column in row:  # for each row iterate through each column
            if column == "X":  # to find "X"
                count += 1  # if found increment count by 1
    return count


def move(board, name):
    """
    To determine if the coordinates from the player or computer have already
    guessed if so try again. if not, are these coordinates a  hit or miss?

    """
    if board == USER_MOVE_BOARD:  # when board is player move board
        row, column = user_input(USER_MOVE_BOARD, name)  # call function to print out questions to player, assign row, column
        if board[row][column] == "-":  # if coordinates passed have "-" assigned, then display message
            print("You already tried those coordinates. Try Again")
            move(board, name)  # function calls itself so player can guess again
        elif board[row][column] == "X":  # if coordinates passed have "X" assigned
            print("You already tried those coordinates. Try Again")
            move(board, name)  # function calls itself so player can guess again
        elif PC_BOARD[row][column] == "O":  # if coordinates on PC_Board are equal to "O"
            board[row][column] = "X"  # then mark board with "X" for a hit, then display message
            print(f"\n****** THAT WAS A HIT {name} *******\n")

        else:
            board[row][column] = "-"  # mark board with "-" for a miss,then display message
            print(f"\n****** You MISSED {name} *******\n")

    elif board == PC_MOVE_BOARD:
        row, column = random.randint(0, 7), random.randint(0, 7)  # randomly assign values to row, column
        if board[row][column] == "-":  # if coordinates passed have "-" assigned
            move(board, name)  # function calls itself so computer can guess again
        elif board[row][column] == "X":  # if coordinates passed have "X" assigned
            move(board, name)  # function calls itself so computer can guess again
        elif USER_BOARD[row][column] == "O":  # if coordinates on USER_BOARD are equal to "O"
            board[row][column] = "X"  # then mark board with "X" for a hit, then display message
            print("***** The Computer Got A Hit ******")
        else:
            board[row][column] = "-"  # mark board with "-" for a miss,then display message
            print("\n****** The Computer MISSED *******\n")


def game():
    """
    Starts a new game. Displays logo and calls function for user and computer to populate boards.
    Displays text and call functions for each round.
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
    name = user_name()  # player name is assinged to name
    location_ships(PC_BOARD, name)
    #print_board(PC_BOARD)# to display the computers board with populated ships (for testing purposes)
    print(f"{name}\'s Board")
    print_board(USER_BOARD)  # players board  is printed
    location_ships(USER_BOARD, name)  # called to allow the user to populate board
    round = 1   # value to count round
    while True:
        while True:
            print(f" ----- ROUND {round} -----")
            print(" ")
            hits_needed = sum(NUMBER_OF_SHIPS)
            # to track the scores of both Player and Computer
            print(f"{name} Score: {hit_counter(USER_MOVE_BOARD)}/{hits_needed} vs Computer Score: {hit_counter(PC_MOVE_BOARD)}/{hits_needed}")
            print(f"\n -- {name}'s Move --\n")
            print(f"{name}\'s Guess Board")
            print_board(USER_MOVE_BOARD)  # call function print_board and passed USER_MOVE_BOARD
            move(USER_MOVE_BOARD, name)
            round += 1  # round is incremented by 1
            break
        if hit_counter(USER_MOVE_BOARD) == 17:  # if Player gets counter to 17, messages are print
            print("*"*10, f"{name} IS THE WINNER ", "*"*10)
            print("*"*10, f"Congratulations {name} ", "*"*10)
            break

        while True:
            print("\n-- Computer Turn --\n")
            print(f"Computer\'s Guess Board")
            move(PC_MOVE_BOARD, name)
            break
        print_board(PC_MOVE_BOARD)
        if hit_counter(PC_MOVE_BOARD) == 17:  # if computer gets counter to 17, messages are print
            print("*"*10, " THE COMPUTER WIN'S ", "*"*10)
            print("*"*10, f" BETTER LUCK NEXT TIME {name} ", "*"*10)
            break


game()  # called to start new game
