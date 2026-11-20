import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    comp_score = 0
    ties = 0
    rounds = 5

    print("=========================================")
    print("   ROCK, PAPER, SCISSORS (BEST OF 5)     ")
    print("=========================================")

    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} of {rounds} ---")
        
        while True:
            user_choice = input("Enter rock, paper, or scissors: ").strip().lower()
            if user_choice in choices:
                break
            print("Invalid choice! Please type 'rock', 'paper', or 'scissors'.")

        comp_choice = random.choice(choices)
        print(f"Computer chose: {comp_choice}")

        if user_choice == comp_choice:
            print("Result: It's a tie!")
            ties += 1
        elif (
            (user_choice == "rock" and comp_choice == "scissors") or
            (user_choice == "paper" and comp_choice == "rock") or
            (user_choice == "scissors" and comp_choice == "paper")
        ):
            print("Result: You win this round!")
            user_score += 1
        else:
            print("Result: Computer wins this round!")
            comp_score += 1

    # Final Scoreboard
    print("\n=========================================")
    print("              FINAL SCOREBOARD           ")
    print("=========================================")
    print(f"Your Wins     : {user_score}")
    print(f"Computer Wins : {comp_score}")
    print(f"Ties          : {ties}")
    print("-----------------------------------------")

    if user_score > comp_score:
        print("CONGRATULATIONS! You are the overall champion!")
    elif comp_score > user_score:
        print("COMPUTER WINS! Better luck next time.")
    else:
        print("IT'S A DRAW! Well played.")

if __name__ == "__main__":
    play_game()