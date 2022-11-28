import random
scores = {"COMPUTER": 0 , "PLAYER" :0}

class Board:
    """

    """
    def __init__( self,size, num_ships,name, type):

        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guess = []
        self.ships =[]

    
    #def guess(self,x,y):
    
   

    #def add_ship(self,x,y type = 'COMPUTER'):
    
    #def random_point(size):
   
    #return randint(0, size -1)
    
    #def populate_board():
    
    #def make_guess():
    
    #def play_game(compBoard,playerBoard):
    
    
    def game():
        """

        """

        size = 2
        num_ships= 2
        scores['COMPUTER'] = 0
        scores['PLAYER'] = 0

        print("-"*40)
        print("      ***** BATTLESHIPS *****     ")
        print("-"*40)
        
        print()
        
        for col_num in range(1):
            print('  | A | B | C | D | E | F | G | H |')

            for row_num in range(1,9):
                print("  ","---"*11)
                print(row_num,"|",  "  | "*8)
                #print("%d|%s|" % (row_num, "|".join(row)))
            
        print()
        print('-'*40)
        print(f"Board size: {size}. number of ships {num_ships}")
        print("-"*40)
        compBoard = Board(size, num_ships, 'computer', type = "COMPUTER")
        playerBoard = Board(size, num_ships, user_name, type= "PLAYER") 


    game()
        
        

