import random


#------------------------------------------------------------------------- DICE
# Simulate 2 separate 6 sided dice rolls
def roll_1 ():
    min_value=1
    max_value=6
    roll_1= random.randint(min_value,max_value)
    # Returns the variable "roll" to the rest of the system
    return roll_1

def roll_2 ():
    min_value=1
    max_value=6
    roll_2= random.randint(min_value,max_value)
    return roll_2

#-------------------------------------------------------------------------- ART
win_art = r'''


██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗    ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║    ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║    ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║    ╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║    ██╗
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝    ╚═╝                                                             
                                        
'''
lose_art = r'''


▓██   ██▓ ▒█████   █    ██     ██▓     ▒█████    ██████ ▓█████ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓██▒    ▒██▒  ██▒▒██    ▒ ▓█   ▀ 
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██░    ▒██░  ██▒░ ▓██▄   ▒███   
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ▒██░    ▒██   ██░  ▒   ██▒▒▓█  ▄ 
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░██████▒░ ████▓▒░▒██████▒▒░▒████▒
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░    ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░ ░   ░ ░ ░ ▒  ░  ░  ░     ░   
 ░ ░         ░ ░     ░            ░  ░    ░ ░        ░     ░  ░
 ░ ░                                                           
                                        
'''
dice_art = r'''
Art by Joan G. Stark
       .-------.    ______
      /   o   /|   /\     \
     /_______/o|  /o \  o  \
     | o     | | /   o\_____\
     |   o   |o/ \o   /o    /
     |     o |/   \ o/  o  /
     '-------'     \/____o/
'''


#------------------------------------------------------------------------ RULES
rules = '''
How to play:

1. Rolling Dice:
    Both players roll two die.

2. Choosing the Highest Combination:
    The highest number combination from
    the two dice rolled will be chosen. 
    For instance, if you roll a 4 and a 6, 
    your best combination is 64.

3. Scoring:
    The player with the highest dice 
    combination in that round earns a point.

4. Winning the Game:
    The first player to reach the 
    preselected number of points wins!

            Good luck!

'''
#------------------------------------------------------ GAME START AND SETTINGS
# \x1B[3m = starts italic formatting
# x1B[0m = Ends italic formatting

print(f"{dice_art} Welcome to the game of \x1B[3mBeat That\x1B[0m! \n\n")

# Shows or skips rules
while True:
    hear_rules= input("Would you like to hear the rules? (y/n): ").lower()
    if hear_rules == "y" or hear_rules == "n":
        if hear_rules == "y":
            print(rules)
            break
        else:
            print("\nNot you're first rodeo?\nOkay then lets being!")
            break
    else:
        print("Please type (y/n).\n")

# Ensures a max points of 1-100 is selected
while True:
    max_points = input("\nHow many points to win? (1-100) ")
    if max_points.isdigit():
        max_points= int(max_points) 
        if max_points in range(101):
            print(f"You have selected {max_points} points to win the game. ")
            break
        else:
            print("Must be between 1-100. ")
    else:
        print("Invalid. Enter a number between 1-100 ")

#---------------------------------------------------------- MAIN GAME VARIABLES
player_points = 0

npc_points = 0

round_num = 0

point_reminder = "points needed to win:"
# Points needed to win
npc_goal = max_points - npc_points

player_goal = max_points - player_points                    

#--------------------------------------------------------------- MAIN GAME LOOP
while player_points < max_points and npc_points < max_points:

    print("\n---Your turn!---")
    round_num += 1

    should_roll = input ("Would you like to roll (y)? ").lower()
    if should_roll == "y":
        value_1 = roll_1()
        value_2 = roll_2()

        # Ensures die combonation is max value
        if value_1 >= value_2:
            player_dice_score = (value_1 * 10) + value_2
        else:
            player_dice_score = (value_2 * 10) + value_1

        print(f"\nYou rolLed a {value_1} and a {value_2}. \
        \nYour max score is: {player_dice_score}\n\n---NPC's turn!---")
        
        value_1 = roll_1()
        value_2 = roll_2()

        if value_1 >= value_2:
            npc_dice_score = (value_1 * 10) + value_2
        else:
            npc_dice_score = (value_2 * 10) + value_1

        print(f"The NPC rolLed a {value_1} and a {value_2}. \
        \nTheir max score is:{npc_dice_score}\n\n---Round results---")

        if player_dice_score > npc_dice_score:
            player_points += 1
            
            print(f"You won this round! \nYou now have {player_points} points.")

        elif player_dice_score < npc_dice_score:
            npc_points += 1
           
            print(f"You lost this round!\nThe NPC now has {npc_points} points.")
        
        else:
            print(f"You tied round!\n No one gains any points.\
            \nYour points:{player_points}")
        
        npc_goal = max_points - npc_points
        player_goal = max_points - player_points
        
        print(f"\n---Stats---\nThier {point_reminder} {npc_goal}\
        \nYour {point_reminder} {player_goal}\n\n---End of Round {round_num}---")

        if player_points == max_points:
            print(win_art)

        elif npc_points == max_points:
            print(lose_art)
            break
        else:
            print("\n") #without this makes the elif statment below not work?

    elif should_roll == "n" or should_roll == "no": 
         print("Okay rude...")
         quit()

    else:
        print("Invalid input.")

#----------------------------------END GAME-------------------------------------

