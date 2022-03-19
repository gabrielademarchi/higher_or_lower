from art import logo, vs
from game_data import data
import os
import random


def clear():
    return os.system('cls')


def create_pair():
    return random.sample(data, 2)


def compare_followers(dict1, dict2):
    if dict1["follower_count"] > dict2["follower_count"]:
        return 1
    else:
        return 0


def update_pair(lista):
    new_profile = random.choice(data)
    while new_profile in lista:
        new_profile = random.choice(data)
    follower_index = compare_followers(lista[0], lista[1])
    lista.pop(follower_index)
    lista.append(new_profile)
    return lista


def prin_comparison(subjects):
    print(
        f'Compare A: {subjects[0]["name"]}, a {subjects[0]["description"]}, from {subjects[0]["country"]}')

    print(vs)

    print(
        f'Against B: {subjects[1]["name"]}, a {subjects[1]["description"]}, from {subjects[1]["country"]}')


def change_guess_index(guess):
    '''change guess to subjects index with less followers'''
    if guess == 'a':
        return 1
    else:
        return 0


def run_game():
    print(logo)
    game_over = False
    score = 0
    subjects = create_pair()

    while not game_over:

        prin_comparison(subjects)

        answer = compare_followers(subjects[0], subjects[1])

        guess = input("Who has more followers? type 'A' or 'B': ").lower()
        guess = change_guess_index(guess)

        clear()

        if guess == answer:
            score += 1
            subjects = update_pair(subjects)
            print(logo)
            print(f"You're right! Current score: {score}")
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score {score}")
            game_over = True


run_game()
