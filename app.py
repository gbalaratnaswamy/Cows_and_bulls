import game_lib

print("""
==================================================================
                       COWS AND BULLS
==================================================================
""")
level = int(input("""enter difficulty level(number)
1 easy 
2 medium
3 hard
4 insane
"""))
rand_digit = game_lib.start_game()
num_of_times = 0
max_num_of_times = 14 - level * 2
while num_of_times < max_num_of_times:
    guess_number = game_lib.num_to_digits(int(input("enter your guess number : ")))
    num_cows, num_bulls = game_lib.play_game(rand_digit, guess_number)
    num_of_times += 1
    print(f"no of cows is {num_cows} and no of bulls is {num_bulls}")
else:
    print(f"you lose you took too many attempts and number is {game_lib.array_to_num(rand_digit)}")
