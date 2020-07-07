import game_lib
from random import random

print("""
==================================================================
                       COWS AND BULLS
==================================================================
""")

rand_digit = game_lib.start_game()
guess_answers = game_lib.full_matrix_generator()
guess = 1234
while True:
    guess_number = game_lib.num_to_digits(int(input("enter your guess number : ")))
    num_cows, num_bulls = game_lib.play_game(rand_digit, guess_number)
    if num_cows == 4:
        print("you won")
        break
    print(f"no of cows is {num_cows} and no of bulls is {num_bulls}")
    print(f"guess number is {guess}")
    cows_in = int(input("enter cows : "))
    bulls_in = int(input("enter bulls : "))
    if cows_in == 4:
        print("you lose")
        break
    i = 0
    while i < len(guess_answers):
        cows_temp, bulls_temp = game_lib.play_game(game_lib.num_to_digits(guess_answers[i]), game_lib.num_to_digits(guess))
        if cows_temp != cows_in or bulls_temp != bulls_in:
            guess_answers.remove(guess_answers[i])
            i -= 1
        i += 1
    r = int(random() * len(guess_answers))
    guess = guess_answers[r]
