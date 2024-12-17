import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break


guess_the_number()

import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    score = 0
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = input("Enter 'rock', 'paper', or 'scissors' (or 'quit' to exit): ").lower()

        if user_choice == 'quit':
            print(f"Thanks for playing! Your total score is: {score}")
            break

        if user_choice not in choices:
            print("Invalid choice, try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
            score += 1
        else:
            print("You lose!")

rock_paper_scissors()

# 3. Magic 8-Ball
import random

def magic_8_ball():
    responses = [
        "Yes, definitely!", "No way!", "Maybe...", "Ask again later.",
        "It is certain.", "Very doubtful.", "Outlook not so good.", "Signs point to yes."
    ]
    print("Welcome to the Magic 8-Ball!")
    while True:
        question = input("Ask a yes/no question (or 'quit' to exit): ")
        if question.lower() == "quit":
            break
        print(random.choice(responses))

magic_8_ball()

# 4. Number Guessing with Limited Attempts (with Points)
import random
def limited_attempts_guess():
    target = random.randint(1, 50)
    attempts = 5
    score = 0
    print("Guess the number between 1 and 50. You have 5 attempts!")

    while attempts > 0:
        guess = int(input("Enter your guess: "))
        attempts -= 1
        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            print("Correct! You win!")
            score += 1
            print(f"Your total score is: {score}")
            return
        print(f"Attempts left: {attempts}")
    print(f"Out of attempts! The number was {target}. Your total score is: {score}")

limited_attempts_guess()

# 5. Dice Roller
import random
def dice_roller():
    score = 0
    print("Welcome to the Dice Roller!")
    while True:
        roll = input("Roll the dice? (y/n): ").lower()
        if roll == 'y':
            print("You rolled a:", random.randint(1, 6))
        elif roll == 'n':
            print(f"Goodbye!")
            break
        else:
            print("Invalid input, try again.")

dice_roller()

# 6. Odd or Even Guessing Game (with Points)
import random

def odd_or_even():
    score = 0
    print("Welcome to Odd or Even!")
    while True:
        player_guess = input("Guess 'odd' or 'even' (or 'quit' to exit): ").lower()
        if player_guess == 'quit':
            print(f"Thanks for playing! Your total score is: {score}")
            break
        if player_guess not in ["odd", "even"]:
            print("Invalid choice, try again.")
            continue

        number = random.randint(1, 100)
        print(f"The number is: {number}")

        if (number % 2 == 0 and player_guess == "even") or (number % 2 != 0 and player_guess == "odd"):
            print("You guessed right!")
            score += 1
        else:
            print("Wrong guess!")

odd_or_even()

# 7. Word Scramble (with Points)
import random

def word_scramble():
    words = ["python", "random", "scramble", "function", "computer"]
    word = random.choice(words)
    scrambled = ''.join(random.sample(word, len(word)))
    score = 0
    print("Unscramble the word:", scrambled)
    guess = input("Your guess: ")

    if guess == word:
        score += 1
        print("Correct! You win!")
    else:
        print(f"Wrong! The word was: {word}")
    print(f"Your total score is: {score}")

word_scramble()

# 8. Simple Math Quiz (with Points)
import random

def math_quiz():
    score = 0
    print("Welcome to the Math Quiz!")
    while True:
        for _ in range(5):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            operation = random.choice(["+", "-", "*"])
            question = f"{num1} {operation} {num2}"
            answer = eval(question)
            user_answer = int(input(f"What is {question}? Answer: "))

            if user_answer == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The answer is {answer}")

        print(f"Your score for this round is: {score}/5")

        continue_game = input("Do you want to play another round? (yes/no): ").strip().lower()
        if continue_game != 'yes':
            print(f"Thanks for playing! Your total score is: {score}")
            break
        else:
            score = 0

math_quiz()

# 9. Tic Tac Toe
def display_board(board):
    print("\n".join([" | ".join(row) for row in board]))
    print()  # Add an extra newline for readability

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    moves = 0
    print("Welcome to Tic-Tac-Toe! Enter your move as 'row,column' (e.g., '0,2').")
    while moves < 9:
        display_board(board)
        print(f"Player {player}'s turn")
        try:
            row, col = map(int, input("Enter row and column (0,1,2): ").split(","))
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid position! Please enter values between 0 and 2.")
                continue
            if board[row][col] != " ":
                print("Cell already taken. Try a different position.")
                continue
            board[row][col] = player
            moves += 1
            if check_win(board, player):
                display_board(board)
                print(f"Player {player} wins!")
                return
            player = "O" if player == "X" else "X"
        except ValueError:
            continue
    display_board(board)
    print("It's a draw!")

tic_tac_toe()
