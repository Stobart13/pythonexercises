#Get player names
player_1 = input("Enter player 1 name: ")
player_2 = input("Enter player 2 name: ")

#Used for debugging
# print ("Player 1 name is: " +player_1)
# print ("Player 2 name is: " +player_2)

#Sets int value for each option, will error if rock, paper of scissors is not selected
game_dictionary = {"rock" : 1, "paper": 2, "scissors": 3}

while True:
    # Player makes selection
    player_1_choice = str(input("%s, Please select Rock, Paper or Scissors: " %player_1))
    player_2_choice = str(input("%s, Please select Rock, Paper or Scissors: " %player_2))
    
    #this gets the int value based on what the user has inputted, used .lower() to make option case insensitive when user inputs
    p1 = game_dictionary.get(player_1_choice.lower())
    p2 = game_dictionary.get(player_2_choice.lower())
    
    # gets the difference between player 1 and player 2 to work out winner
    dif = p1 - p2
    
    # used for debugging
    # print(dif)
    
    
    if dif in [-2, 1]:
        print("%s is the winner! Well Done!" %player_1)
        if str(input('Do you want to play again?\n')) == 'yes':
            continue
        else:
            print('Game over.')
            break
    elif dif in [-1, 2]:
        print("%s is the winner! Well Done!" %player_2)
        if str(input('Do you want to play again?\n')) == 'yes':
            continue
        else:
            print('Game over.')
            break
    else:
        print("Its a draw! Keep playing")
        print("")