def prRed(skk): print("\033[91m {}\033[00m" .format(skk))


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))


def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))


def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))


def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))


def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))


def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
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
        prRed("Okay, bye!")
        exit()
    elif answer == "Yes" or answer == "yes":
        prGreen("Lets play!")
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
    prGreen("Lets play!")
    win = False
    while True:
        print("Choose your move:")
        player_one_input = input()
        computer_input = random.choice(choices)
        if player_one_input == "rock" and computer_input == "rock":
            print(f"Computer choose:{computer_input}")
            prYellow("Draw")
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
            prYellow("Draw")
            continue
        elif player_one_input == "scissors" and computer_input == "scissors":
            print(f'Computer choose:{computer_input}')
            prYellow("Draw")
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
        prCyan("Congratulations! You win!")
    else:
        prRed(f"{computer} wins")
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
            prYellow("Draw")
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
            prYellow("Draw")
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
            prYellow("Draw")
        else:
            raise SystemExit("Invalid input ! Try again ...")

    if player_wins_counter > computer_wins_counter:
        prCyan("Congratulations! You win!")
        print(f"Player:{player_wins_counter} - Computer {computer_wins_counter}")
    else:
        prRed("Computer wins!")
        print(f"Computer:{computer_wins_counter} - Player:{player_wins_counter}")

print(f"Thank you for playing {player_name}! See you soon!")
