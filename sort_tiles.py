#this will be a 4x4 grid of tiles that are lettered a-o plus a 'blank tile' that will occupy the 16th space
# they will look like the following:
#     KEYS      |   VALUES
#  1  2  3  4   | a  b  c  d
#  5  6  7  8   | e  f  g  h
#  9 10 11 12   | i  j  k  l
# 13 14 15 16   | m  n  o  _
# I plan to use a dictionary and with key value pairs where the keys are 1-16 (16 letters of the alphabet) 
## and the values are the numbers a-o as strings and a blank which
# To start with a random board I will randomly assign a value to each letter and whichever one gets p will be replaced with " "
# Users will then use the arrow keys to "move" tiles around and get them into the correct order 
# after each move the board will "check for a win" and the game will end once the user wins OR they can hit Q to quit at anytime
## press an arrow and first check if it's a valid move: 
## if up IS "blank key + 4" <= 16
## if down then US "blank key - 4" >= 1
## if right IS "blank key" == 4, 8, 12, 16
## if left IS "Blank Key" == 1, 5, 9, 13
##IF YES then make move
## if q: quit
## if up then swap blank with "Blank Key" value becomes "blank key + 4" value & "Blank Key + 4" becomes blank
## if down then swap blank with "Blank Key" value becomes "blank key - 4" value & "Blank Key - 4" becomes blank
## if right then swap blank with "Blank Key" value becomes "blank key - 1" value & "Blank Key - 1" becomes blank
## if left then swap blank with "Blank Key" value becomes "blank key + 1" value & "Blank Key + 1" becomes blank
##if NO print(That is not a valid move)

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', '_']
# board = {1:'', 2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:'', 9:'', 10:'', 11:'', 12:'', 13:'', 14:'', 15:'', 16:''}

import random
from pynput import keyboard

def make_board(start):
    if start == "GO":
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', '_']
        board = {1:'', 2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:'', 9:'', 10:'', 11:'', 12:'', 13:'', 14:'', 15:'', 16:''}
        for space in board:
            board[space] = random.choice(letters)
            letters.remove(board[space])
        print_board(board)
        return board

def print_board(board):
    row_1 = board[1]+' '+board[2]+' '+board[3]+' '+board[4]
    row_2 = board[5]+' '+board[6]+' '+board[7]+' '+board[8]
    row_3 = board[9]+' '+board[10]+' '+board[11]+' '+board[12]
    row_4 = board[13]+' '+board[14]+' '+board[15]+' '+board[16]
    print(row_1)
    print(row_2)
    print(row_3)
    print(row_4)
    return 

def check_win(current_board):
    winning_board = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'_'}
    if current_board == winning_board:
        print("YOU WIN!")
        playing = False

## if up IS "blank key + 4" <= 16
## if down then US "blank key - 4" >= 1
## if right IS "blank key" == 4, 8, 12, 16
## if left IS "Blank Key" == 1, 5, 9, 13
def check_valid_move(board, move):
    pass

#a user will press up, down, left, right, or q to quit
def get_move(move):
    pass

def on_press(key):
    if key == keyboard.Key.up:
        move = "up"
    elif key == keyboard.Key.down:
        move = "down"
    elif key == keyboard.Key.left:
        move = "left"
    elif key == keyboard.Key.right:
        move = "right"
    return move

### GAMEPLAY ###
# This sets up the board and saves it to variable that we can manipulate in game play
# playing = True

# while playing:
#     current_board = make_board("GO")
#     move = on_press()
#     if check_valid_move(current_board, move):


    
    
