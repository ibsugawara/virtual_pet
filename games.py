import random

def word_game():
    words = ["cheese", "banana", "butter", "monkey", "rabbit", "travel", "bottle", "animal"]
    letter_board = ["_"] * 6
    tries = 0

    print("Welcome to the Word Game!\nYou have 8 tries to discover the mistery word.")
    answer = random.choice(words)
    print(" ".join(letter_board))

    while tries != 8:
        guess = input("Guess a letter!\n>> ").lower()
        if len(guess) != 1:
            print("Invalid input.")
            continue

        tries += 1
        print(f"You have {8 - tries} tries left.")
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    letter_board[i] = guess
                    print(" ".join(letter_board))
        else:
            print(f'Theres no "{guess}" in this word!')
            print(" ".join(letter_board))
        if "_" not in letter_board:
            print("You won the game!")
            return "won"