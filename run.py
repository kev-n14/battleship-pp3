import random
scores = {"COMPUTER": 0 , "PLAYER" :0}

class Board:
    """

    """

    def __init__(self,size, num_ships,name, type):

        self.size = size
        self.board = [["." for x in range(size)]] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guess = []
        self.ships. =[]

    def print(self):
        for row in sewlf.board:
            print(" ".join(row))
    
    def game():
        """

        """
        size = 2
        num_ships= 2
        scores['COMPUTER'] = 0
        scores['PLAYER'] = 0

        print("-"*30)
        print(" BATTLESHIPS ")
        print(f"Board size: {size}. number of ships{num_ships}")
        print("-"*30)
        compBoard = Board(size, num_ships, 'computer', type = "COMPUTER")
        playerBoard = Board(size, num_ships, user_name, type= "PLAYER") 
        
        


