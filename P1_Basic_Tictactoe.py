import os
import time
import random

gamestate = True
TicTacToe = False
results = 0
game_board = [[0, 0, 0],  [0, 0, 0], [0, 0, 0]]

def invalid_response():
    print ("Please enter a valid response! \n")
    time.sleep(2)

def make_move(move_X = 3, move_Y = 3,display = False, legal_move = False):
    if display == False:
        while legal_move == False:
            global game_board
            print ('Please make your move: \n')
            move_X = 3
            move_Y = 3
            print ("   a  b  c")
            for count, row in enumerate (game_board) :
                print (count, row)
            print ("\n")
            while move_X not in [0, 1, 2]:
                move_X = input ('Please enter the X coordinates: \n')
                if move_X == 'a':
                    move_X = int(0)
                elif move_X == 'b':
                    move_X = int(1)
                elif move_X == 'c':
                    move_X = int(2)
                else:
                    invalid_response()
                    move_X = int(3)
            while move_Y not in [0, 1, 2]:
                move_Y = input ('Please enter the Y coordinates: \n')
                if move_Y == '0':
                    move_Y = int(0)
                elif move_Y == '1':
                        move_Y = int(1)
                elif move_Y == '2':
                    move_Y = int(2)
                else:
                    invalid_response()
                    move_Y = int(3)
            if game_board[move_Y][move_X] == 0:
                game_board[move_Y][move_X] = 1
                os.system('cls')
                print ("   a  b  c")
                for count, row in enumerate (game_board) :
                    print (count, row)
                print ("\n")
                legal_move = True
            else:
                if move_X == int(0):
                    move_X = 'a'
                elif move_X == int(1):
                    move_X = 'b'
                elif move_X == int(2):
                    move_X = 'c'
                print(move_X, move_Y, " is an illegal move.\n")

    else:
        game_board = [[0, 0, 0],  [0, 0, 0], [0, 0, 0]]
        print ("   a  b  c")
        for count, row in enumerate (game_board) :
            print (count, row)
        print ("\n")

def random_bot(bot_moved = 0):
    global game_board
    while bot_moved == 0:
        move_Y = int (random.randint (0, 2))
        move_X = int (random.randint (0, 2))
        if game_board[move_Y][move_X] == 0:
            game_board[move_Y][move_X] = 2
            os.system('cls')
            print ("   a  b  c")
            for count, row in enumerate (game_board) :
                print (count, row)
            print ("\n")
            bot_moved = 1

def check_gamestate(winner = 0): #checks for a winner in the game. Returns result in "results" as 0 (no winner), 1 (player), 2 (bot)
    global results
    for row in game_board: #determine winner from each row
        if row.count(row[0]) == len(row) and row[0] == 1:
            winner = 1
            results = 1
        elif row.count(row[0]) ==len(row) and row[0] == 2:
            winner = 2
            results = 2
    for col_i in range(len(game_board)): #determine winner from each column
        col = []
        for row in game_board:
            col.append(row[col_i])
        if col.count(col[0]) == len(col) and col[0] == 1:
            winner = 1
            results = 1
        elif col.count(col[0]) == len(col) and col[0] == 2:
            winner = 2
            results = 2
    diag1 = []
    for row in game_board:
        diag1.append(game_board[len(diag1)][len(diag1)])
    if diag1.count(diag1[0]) == len(diag1) and diag1[0] == 1:
        winner = 1
        results = 1
    elif diag1.count(diag1[0]) == len(diag1) and diag1[0] == 2:
        winner = 2
        results = 2
    diag2 = []
    for row in game_board:
        diag2.append(game_board[len(game_board)-(1 + len(diag2))][len(diag2)])
    if diag2.count(diag2[0]) == len(diag2) and diag2[0] == 1:
        winner = 1
        results = 1
    elif diag2.count(diag2[0]) == len(diag2) and diag2[0] == 2:
        winner = 2
        results = 2    
            
while gamestate == True:

    os.system('cls')
    start = str.upper (input ("Would you like to play a game of tic-tac-toe? (Y/N): \n"))
    if start == "Y":
        TicTacToe = True
    elif start == "N":
        os.system ('cls')
        gamestate = False
        TicTacToe = False
    else:
        invalid_response()
        TicTacToe = False

    while TicTacToe == True:
        os.system ('cls')
        print ('This is a single-player game of tic-tac-toe played between a user and a very basic AI. \n')

        current_move = 0
        winner = 0
        print ('This is the game board: \n')
        game_board = [[0, 0, 0],  [0, 0, 0], [0, 0, 0]]
        print ("   a  b  c")
        for count, row in enumerate (game_board) :
            print (count, row)
        print ("\n")
        time.sleep (2)

        os.system ('cls')

        while current_move < len(game_board)*len(game_board) and results == 0:
            make_move()
            current_move += 1
            check_gamestate()
            os.system ('cls')
            random_bot()
            current_move += 1
            check_gamestate()
            os.system ('cls')
        if results == 1:
            print ('You win!')
            time.sleep (2)
            results = 0
            TicTacToe = False
        elif results == 2:
            print ('You lose!')
            time.sleep (2)
            results = 0
            TicTacToe = False
        else:
            print ('Draw!')
            time.sleep (2)
            results = 0
            TicTacToe = False

exit()