from random import randint
from random import random

def start_game():
    rand_num = []
    while len(rand_num) < 4:
        num = randint(1, 9)
        if num not in rand_num:
            rand_num.append(num)
    return rand_num


def array_to_num(a):
    return a[3] * 1000 + a[2] * 100 + a[1] * 10 + a[0]


def num_to_digits(a):
    num = []
    for digit in range(4):
        num.append(a % 10)
        a = a // 10
    return num


def play_game(rand_digit, guess_number):
    num_cows = 0
    num_bulls = 0
    for i in range(4):
        for j in range(4):
            if guess_number[j] == rand_digit[i]:
                if i == j:
                    num_cows += 1
                else:
                    num_bulls += 1
                break
    return num_cows, num_bulls


def full_matrix_generator():
    full_matrix = []
    for i in range(1, 10):
        for j in range(1, 10):
            if i == j:
                continue
            for k in range(1, 10):
                if k == j or k == i:
                    continue
                for l in range(1, 10):
                    if l == k or l == j or l == i:
                        continue
                    full_matrix.append(i * 1000 + j * 100 + k * 10 + l)
    return full_matrix
