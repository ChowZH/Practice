import random

Gamestate = 1

def Guess_the_Number ():
    Answer = random.randint(1, 20)
    Player_Guess = 0
    print ('The answer is a number between 1 and 20.\n')
    while Player_Guess != Answer:
        Player_Guess = input ('Please give your best guess!\n')
        try:
            if_int = int(Player_Guess)
            Player_Guess = int (Player_Guess)
            if 1 <= Player_Guess <= 20:
                if Player_Guess < Answer:
                    print ('Try going higher.\n')
                elif Player_Guess > Answer:
                    print ('Try going lower.\n')
                else:
                    pass
            else:
                print ('Please provide a valid answer. (Any numebr between 1 and 20)')
        except ValueError:
            print ('Please provide a valid answer. (Any numebr between 1 and 20)')
    print ('Congratulations! {0} is the correct answer!\n' .format (Player_Guess))
    return True

while Gamestate == 1:
    start = input ('Would you like to play a game of Guess the Number? (Y/N)\n')
    if start == 'Y':
        Guess_the_Number()
    elif start == 'N':
        Gamestate = 0
    else:
        print ('Press "Y" to start the game.\n')
        Gamestate = 1