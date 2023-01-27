import random

# Main Menu
print("Enter your name:")
player_name = input()
computer = "Computer"
print(f"Welcome {player_name}")
choices = ["rock", "paper", "scissors"]
print("Do you want to play a game?")
answer = input()

while True:
    if answer == "No" or answer == "no":
        print("Okay, bye!")
        exit()
    elif answer == "Yes" or answer == "yes":
        print("Lets play!")
        break
    else:
        raise SystemExit("Invalid input. Try again....")
# Game modes
print("Choose a game mode")
print("Game mode 1 -> (First to win), Game mode 2 -> (Two out of three)")
game_mode = input()

# Game mode -> 1
if game_mode == '1':
    print("Game mode 1 -> First to win")
    print("Lets play!")
    win = False
    while True:
        print("Choose your move:")
        player_one_input = input()
        computer_input = random.choice(choices)
        if player_one_input == "rock" and computer_input == "rock":
            print(f"Computer choose:{computer_input}")
            print("Draw")
            continue
        elif player_one_input == "rock" and computer_input == "paper":
            print(f"Computer choose:{computer_input}")
            break
        elif player_one_input == "rock" and computer_input == "scissors":
            print(f"Computer choose:{computer_input}")
            win = True
            break
        elif player_one_input == "paper" and computer_input == "rock":
            print(f"Computer choose:{computer_input}")
            win = True
            break
        elif player_one_input == "paper" and computer_input == "scissors":
            print(f"Computer choose:{computer_input}")
            break
        elif player_one_input == "paper" and computer_input == "paper":
            print(f"Computer choose:{computer_input}")
            print("Draw")
            continue
        elif player_one_input == "scissors" and computer_input == "scissors":
            print(f'Computer choose:{computer_input}')
            print("Draw")
            continue
        elif player_one_input == "scissors" and computer_input == "paper":
            print(f"Computer choose:{computer_input}")
            win = True
            break
        elif player_one_input == "scissors" and computer_input == "rock":
            print(f"Computer choose:{computer_input}")
            break
        else:
            raise SystemExit("Invalid input! Try again ...")

    if win:
        print("Congratulations! You win!")
    else:
        print(f"{computer} wins")
# Game mode - > 2
if game_mode == "2":
    print("Game mode 2 -> Two out of three")
    print("Lets play!")
    player_wins_counter = 0
    computer_wins_counter = 0
    while player_wins_counter < 2 and computer_wins_counter < 2:
        print("Choose your move:")
        player_one_input = input()
        computer_input = random.choice(choices)
        if player_one_input == "rock" and computer_input == "rock":
            print(f"Computer choose:{computer_input}")
            print("Draw")
        elif player_one_input == "rock" and computer_input == "paper":
            print(f"Computer choose:{computer_input}")
            computer_wins_counter += 1
            print(f"Player:{player_wins_counter} - Computer:{computer_wins_counter}")
        elif player_one_input == "rock" and computer_input == "scissors":
            print(f"Computer choose:{computer_input}")
            player_wins_counter += 1
            print(f"Player:{player_wins_counter} - Computer:{computer_wins_counter}")
        elif player_one_input == "paper" and computer_input == "rock":
            print(f"Computer choose:{computer_input}")
            player_wins_counter += 1
            print(f"Player:{player_wins_counter} - Computer:{computer_wins_counter}")
        elif player_one_input == "paper" and computer_input == "scissors":
            print(f"Computer choose:{computer_input}")
            computer_wins_counter += 1
            print(f"Player:{player_wins_counter} - Computer:{computer_wins_counter}")
        elif player_one_input == "paper" and computer_input == "paper":
            print(f"Computer choose:{computer_input}")
            print("Draw")
        elif player_one_input == "scissors" and computer_input == "rock":
            print(f"Computer choose:{computer_input}")
            computer_wins_counter += 1
            print(f"Player:{player_wins_counter} - Computer:{computer_wins_counter}")
        elif player_one_input == "scissors" and computer_input == "paper":
            print(f"Computer choose:{computer_input}")
            player_wins_counter += 1
            print(f"Player:{player_wins_counter} - Computer:{computer_wins_counter}")
        elif player_one_input == "scissors" and computer_input == "scissors":
            print(f"Computer choose:{computer_input}")
            print("Draw")
        else:
            raise SystemExit("Invalid input ! Try again ...")

    if player_wins_counter > computer_wins_counter:
        print("Congratulations! You win!")
        print(f"Player:{player_wins_counter} - Computer {computer_wins_counter}")
    else:
        print("Computer wins!")
        print(f"Computer:{computer_wins_counter} - Player:{player_wins_counter}")

print(f"Thank you for playing {player_name}! See you soon!")
