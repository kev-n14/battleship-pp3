# Battleship Warzone Game
Battleship Warzone is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

The User has to try and beat the Computer by finding and destorying all 5 of the Computers boats before the Comptuer destorys their ships. The boats take up diferrent sizes ranging from 2 to 4

[Click Here, To see a live version of my project.](https://battleship-kf.herokuapp.com/)
![Site on all Screen Sizes](images/on_all_screens.png)
## How To Play
-----
Battleship Warzone is based on the board game Battleship. You can learn more check here on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)). This version, the player competes against the computer. The user is first invited to place their ships on the board. The player has the oppertunity to place each boat either horizontally of verticle. Then the player is asked on what row and column they would like to place the ship. This process is repeated for each of the 5 ships.

After each ship is placed on the board. The board is displayed with the updated position of the ship the user has just added. The ships are represented as collection of "O". The Player is asked to make their move to try and find the computers ships by ebtering the row and column they would like to select. the ships on the Computers board is hidden from the Player until they hit a ship by correctly guessing the position of a ship. 

When a player hits the a ship this is represented by "X". A miss is represented by "-". The Player and Computer take it in turns to make guesses to try and find and sink each other's ships.
The winner is the player who sinks all of their opponent's battleships first.
## Features
-----
### Existing Features
* Random board generation:
    * the computers ships are randomly placed on the board.
    * The Player can not see where the Comptuer's ships are.
* Accepts input from Player
* allows player to input name.
* Allows the player to position ships on board.
* Play against Computer
* Ships are differnt sizes.
* Keep track of scores of both Player and Computer.
* Input validation and error-handling
    * player cannot enter coordinates outside the size of the board
    * For the row user must enter numbers.
    * For column user must enter a letters.
    * User/computer cannot select same coordinates twice.

### Future Features
* Add message to display when the player hit a ship
* Improve graphics for user interface
## Data Model
-----
 I decided to 
## Testing
-----
I have manually tested this project by :
* passed the code through PEP8 Code Institute validator - no major errors were detected
    * A few minor errors.
* Passing it invalid values that such as strings when numbers are expected, numbers when a string is expected.
* positing the ships out of the parameters of the board.
* Placing two ships in the same location.
* Testing it in my local terminal and the Code Institute Heroku terminal.

### Bugs
Solved Bugs
* 
### Remaining Bugs
* 
### Validator Testing
* [PEP8 Code Institute validator:] (https://pep8ci.herokuapp.com/#)
    * A few minor errors for invalid sequence for the Battleship logo


## Deployment
-----
* 
## Credits
-----
* Code Institute for the deployment terminal and template.
* Wikipedia for details of the Battleships game
* 