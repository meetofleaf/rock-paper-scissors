import os
import getpass

game_dict = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}

def compare(weapon1, weapon2):                              # Weapon comparison Fn
    diff = weapon1 - weapon2

    if diff in [1, -2]: print("Player 1 wins!\n")
    elif diff in [2, -1]: print("Player 2 wins!\n")
    elif diff == 0: print("It's a Tie!\n")
    else: print("Invalid Input! Try Again.\n")


while True:

    print("\nROCK-PAPER-SCISSORS")
    print("```````````````````")
    print("Rock: 1  |  Paper: 2  |  Scissors: 3")
    print("````````````````````````````````````\n")
    
    player1 = int(getpass.getpass("Choose your weapon Player 1: "))
    player2 = int(getpass.getpass("Choose your weapon Player 2: "))

    if player1 and player2 in (1, 2, 3): pass               # Checking for valid inputs
    else: print("Invalid Input!")

    weapon_1 = str(game_dict.get(player1))
    weapon_2 = str(game_dict.get(player2))
    print("\n" + weapon_1 + "   Vs   " + weapon_2)

    compare(player1, player2)                               # Comparing weapons to find the winner
    
    i = input("Enter 'r' to replay  OR  anything else to exit: ")
    if i == 'r':                                     # Replay option
        os.system('cls')
        continue
    else: 
        exit()
