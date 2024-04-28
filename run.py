# import random
# class GameBaord: 
#     def _init_(self,board):
#         self.board=board
    
#     def get_letter_to_numbers();
#         get_letter_to_numbers = {"A":0, "B":1, "C":2 "D":3"E":4 "F":5 "G",6 "H":7}
#         return letter_to_numbers
def createGameBaord(size):
    board=[]
    for i in range(size):
        row= []
        for d in range(size): 
            row.append("$")
        board.append (row)
    return board
    
def displayboard(board):
    for row in board:
        print(' '.join( row))

gameboard=createGameBaord(10)
displayboard(gameboard)
print('Welcome sailor!')   
print('Can you find all the ships in this small square ocean?\n')
print('How does it work?:')
print('Guess where in the game board the three ships are hidden.')
print('You will be asked to type in a guess for row')
print('The top left of the board is row 0 column 0\n')
  
   
def random_line():
    """
    Get three random numbers to choose location(line) for ship
    """
    return random.randrange(5), random.randrange(5), random.randrang
