"""
Rock, Paper , scissor game

1 for rock ,
-1 for paper
0 for scissor

"""

# Mini Rock-Paper-Scissors Game (Improved Pseudo-Random)

choices = {1: "Rock ✊", -1: "Paper 📄", 0: "Scissors ✌️"}

youDict = {"rock": 1, "paper": -1, "scissor": 0}

outcomes = {
    (1, 1): "It's a Draw!",
    (1, -1): "You Win!",
    (1, 0): "You Lose!",
    (-1, 1): "You Lose!",
    (-1, -1): "It's a Draw!",
    (-1, 0): "You Win!",
    (0, 1): "You Win!",
    (0, -1): "You Lose!",
    (0, 0): "It's a Draw!",
}


def save_result(result):
    try:
        with open("game_results.txt", "a") as file:
            file.write(result + "\n")
    except:
        print("Error: Could not save the result.")


def play_game():
    computer_choices = [1, -1, 0]
    total_input_length = 0

    while True:
        user_choice_input = input("Enter your choice (rock, paper, scissor): ").lower()

        if user_choice_input not in youDict:
            print("Invalid choice, please try again.")
            continue

        total_input_length += len(user_choice_input)

        # randomize based of length of input
        index = (total_input_length * len(user_choice_input)) % 3
        computer_choice = computer_choices[index]

        user_choice = youDict[user_choice_input]

        print(f"Computer chose: {choices[computer_choice]}")
        print(f"You chose: {choices[user_choice]}")

        result = outcomes[(computer_choice, user_choice)]
        print(result)

        save_result(result)

        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break


play_game()


""" logic if you pick rock first round rock=4:  = (4 * 4) % 3 = 16 % 3 = 1
so next time if we type paper len=5 so total (previous) 4+ 5 = 9  so (9 * 5) % 3 = 45 % 3 = 0 so computer choice 0 = 1 

"""
