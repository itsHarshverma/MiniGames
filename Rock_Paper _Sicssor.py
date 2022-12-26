import random

user_wins= 0
comp_wins = 0

options = ["Stone", "Paper","Scissors"]

while True:
    user_input = ("Type Stone/Paper/Scissors  OR Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_num = random.randint(0,2)
    computer_pick = options(random_num)
    print("Computer picked", computer_pick + ".")

    if user_input == "stone" and computer_pick == "scissors":
        print("You won!!!!")
        user_wins += 1
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!!!!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!!!!")
        user_wins += 1
    else:
        print("You loose")
        comp_wins+= 1
print("you won", user_wins,"times. ")
print("The computer won", comp_wins,"times.")
print("Goodbye!")



