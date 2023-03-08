import random
import math

n = input('Number of games: ')

def RockPaperScissors(n):
    #try block catches arguments that are not integers
    try:
        n = int(n)

        user_score = 0
        comp_score = 0
        i = 0 

        #set the breaking condition depending on the number of games to be played
        if n % 2 == 0:
            break_cond = n/2 + 1
        else:
            break_cond = math.ceil(n/2)

        while i <n:
            if user_score >= break_cond or comp_score >= break_cond:
            #breaks the game when a user gets more than half the max points
                break


            choices = ['Rock', 'Scissors', 'Paper']
            user_c = str(input("Choose Rock, Paper, or Scissors: ")).lower().capitalize() #format user choice to match choices in list
            comp_c = random.choice(choices)

            #stopping condition and checking if user choice is valid
            #makes user choice into lower case then capitalize to match the choices
            if user_c not in choices:
                if user_c == 'Stop':
                    print('Thanks for playing!')
                    return
                print('Please choose a valid option.')
                continue

            #tuple of computer's and user's choice  
            user_comp_tup = (user_c, comp_c)

            #winning conditions
            win = [('Rock', 'Scissors'), ('Scissors', 'Paper'), ('Paper', 'Rock')]

            #checking for winner in trial
            if user_c == comp_c: #tie does not add to the scores but is counted in trials
                print("It's a tie")
            elif user_comp_tup in win:
                print(f"Computer chose {comp_c.lower()}, you win.")
                user_score += 1
            else:
                print(f"Computer chose {comp_c.lower()}, you lost")
                comp_score += 1

            #show the score
            print(f"You: {user_score}, Computer: {comp_score}")
            i += 1

        #prints out the result of the game
        if user_score > comp_score:
            print("Congrats! You won!")
        elif user_score == comp_score:
            print("It's a tie")
        else:
            print("Sorry, you lost.")
        
        #ask if user wants to play again
        playAgain = input('Want to play again? [y/n]: ')
        if playAgain == 'y':
            n = input('Number of games: ')
            RockPaperScissors(n)
            
    #print an error message if argument is not valid object type and returns the function
    except:
        print("Error: The argument must be of type 'int'")

        n = input('Number of games: ')
        RockPaperScissors(n)

RockPaperScissors(n)

