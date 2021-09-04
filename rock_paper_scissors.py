# rock paper scissors

player_1 = input("Player 1: Rock Paper Or Scissors? ").lower()

player_2 = input("Player 2: Rock Paper Or Scissors? ").lower()


# rock

# both players
if player_1 == "rock" and player_2 == "rock":
    print("Draw!")


# rock scissors

if player_1 == "rock" and player_2 == "scissors":
    print("Player 1 has won!")
elif player_2 == "rock" and player_1 == "scissors":
        print("Player 2 has won!")


# rock paper

if player_1 == "rock" and player_2 == "paper":
    print("Player 2 has won!")
elif player_1 == "paper" and player_2 =="rock":
    print('Player 1 has won!')


# scissors 

if player_1 == 'scissors' and player_2 == 'scissors':
    print('Draw! ')

# scissors paper

if player_1 == "scissors" and player_2 =="paper":
    print('Player 1 has won! ')
elif player_2 == 'scissors' and player_1 == 'paper':
    print('Player 2 has won! ')



# paper

if player_1 == 'paper' and player_2 == 'paper':
    print('Draw! ')
    
else:
    print('Error')
