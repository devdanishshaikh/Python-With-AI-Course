player_1 = input("Player 1, please enter your choice (Rock, Paper, Scissors): ")
player_2 = input("Player 2, please enter your choice (Rock, Paper, Scissors): ")

if player_1 == player_2:
    print("Game Draw!")
else:
    if player_1 == "Rock":
        if player_2 == "Scissors":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    elif player_1 == "Paper":
        if player_2 == "Rock":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    elif player_1 == "Scissors":
        if player_2 == "Paper":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    else:
        print("Invalid input from Player 1.")
