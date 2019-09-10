import os
import getpass

game_dict = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}

score_list = [[],[]]

def score(z):                                                           # Function to keep scores
    global score_list
    if z==0:
        score_list[0].append(1)
        score_list[1].append(0)
    elif z==1:
        score_list[0].append(0)
        score_list[1].append(1)
    elif z==-1:
        score_list[0].append(0)
        score_list[1].append(0)

def compare(weapon1, weapon2):                                          # Weapon comparison Fn
    diff = weapon1 - weapon2

    if diff in [1, -2]:
        print("Player 1 wins!\n")
        score(0)
    elif diff in [2, -1]:
        print("Player 2 wins!\n")
        score(1)
    elif diff == 0:
        print("It's a Tie!\n")
        score(-1)
    else:
        print("Invalid Input! Try Again.\n")


while True:
    print("\nROCK-PAPER-SCISSORS")
    print("```````````````````")
    print("Rock: 1  |  Paper: 2  |  Scissors: 3")
    print("````````````````````````````````````\n")
    
    player1 = int(getpass.getpass("Choose your weapon Player 1: "))     # Player 1 chooses a weapon
    player2 = int(getpass.getpass("Choose your weapon Player 2: "))     # Player 2 chooses a weapon

    if player1 and player2 not in (1, 2, 3):                            # Checking for valid inputs
        print("Invalid Input!")
    else:
        weapon_1 = str(game_dict.get(player1))
        weapon_2 = str(game_dict.get(player2))
        print("\n" + weapon_1 + "   Vs   " + weapon_2)

        compare(player1, player2)                                       # Comparing weapons to find the winner
    
    i = input("Enter 'r' to replay  OR  anything else to exit: ")
    if i == 'r':                                                        # Replay option
        os.system('cls')
        continue
    else:
        print("Player 1:" + str(score_list[0]) +", Score: "+ str(score_list[0].count(1)))
        print("Player 2:" + str(score_list[1]) +", Score: "+ str(score_list[1].count(1)))
        exit()
