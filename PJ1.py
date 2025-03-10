# SNAKE, WATER, GUN GAME
# 
# Rules:
# User Selects one of SNAKE, WATER, GUN
#   - SNAKE VS GUN, GUN WINS as gun kills snake
#   - GUN VS WATER, WATER WINS as gun drowns in water
#   - WATER VS SNAKE, SNAKE WINS as snake can escape through water

import random

options = ['w','s','g']

def SWGgame(n):

    com_points = 0
    player_points = 0
    round = 1
    while(round <= n):
        print(f"Round : {round} ")
        c = input("Choose - Snake[s] or Water[w] or Gun[g]: ")
        computer = random.choice(options)
        if(computer == 's' and c == 's' or computer == 'w' and c == 'w' or computer == 'g' and c == 'g'):
            print("Tie")
            round += 1
        elif(computer == 'g' and c == 's'):
            print("Computer Wins")
            com_points += 1
            round += 1
        elif(computer == 'w' and c == 'g'):
            print("Computer Wins")
            com_points += 1
            round += 1
        elif(computer == 's' and c == 'w'):
            print("Computer Wins")
            com_points += 1
            round += 1
        elif(computer == 's' and c == 'g'):
            print("Player Wins")
            player_points += 1
            round += 1
        elif(computer == 'w' and c == 's'):
            print("Player Wins")
            player_points += 1
            round += 1
        elif(computer == 'g' and c == 'w'):
            print("Player Wins")
            player_points += 1
            round += 1
        else:
            print("Invalid Input")
            round += 1

    
    print('--------------------------------------------')
    print(f'Final Score -> | Player = {player_points} | Computer = {com_points} |')
    print('--------------------------------------------')

    if(com_points > player_points):
        print("\t\tComputer Wins")
    elif(com_points < player_points):
        print("\t\tPlayer Wins")
    else:
        print("\t\tIts a TIE")

    print('--------------------------------------------')


print('--------------------------------------------')
print('          SNAKE - WATER - GUN GAME          ')
print('--------------------------------------------')

n = int(input("Enter no. of Rounds: "))
SWGgame(n)






