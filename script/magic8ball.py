import random


def get_answer(number):
    answers = {
        1: "It is certain",
        2: "Yes definitely",
        3: "Most likely",
        4: "Reply hazy, try again",
        5: "Ask again later",
        6: "Cannot predict now",
        7: "Don't count on it",
        8: "My reply is no",
        9: "Very doubtful",
    }
    return answers.get(number, "No fortune found.")


print("Ask a yes or no question:")
input("> ")  # Get user input

r = random.randint(1, 9)
fortune = get_answer(r)
print(fortune)
