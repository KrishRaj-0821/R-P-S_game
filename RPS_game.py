import random
import pyttsx3
print("\n######{__Welcome to Rock, Paper, Scissors!__}######\n")

computer_point, user_point, round = 0, 0, 1

while computer_point < 3 and user_point < 3:
    
    print(f"\n#####__Round {round}__#####\n")
    print("To quit the game, type 'quit' at any time.\n")
    choice = input("Enter your choice\n{'rock', 'paper', 'scissors'}: ") # user choice

    
    if choice not in ["rock", "paper", "scissors", "quit"]:
        print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
        continue
    
    elif choice == "quit":
            print("\n!!GAME OVER!!\n\tGoodbye!\n")
            engine = pyttsx3.init()
            engine.say("GAME OVER!")
            engine.runAndWait()
            break
            
    else:
        computer_choice = random.choice(["rock", "paper", "scissors"])  #ramdom_choice
        print(f"\nComputer chose: {computer_choice}") #{computer's_choice}
        if choice == computer_choice:
            print("***It's a tie!***")
        else:
            if (choice == "rock" and computer_choice == "scissors") or \
            (choice == "paper" and computer_choice == "rock") or \
            (choice == "scissors" and computer_choice == "paper"):
                user_point += 1

            else:
                computer_point += 1
        print(f"\nCurrent Score - You: {user_point}, Computer: {computer_point}")
        round += 1

engine = pyttsx3.init()
if computer_point > user_point:
    print("\nYou Lose!\n")
    engine.say("You Lose!")
elif computer_point == user_point:
    print("\nIt's a Draw!\n")
    engine.say("It's a Draw!")
else:
    print("\nYou Win!\n")
    engine.say("You Win!")
engine.runAndWait()