# Higher or Lower game
import random
from logos import logo
from logos import vs
from data import data

choice_list = random.sample(data, 2)
if choice_list[0] == choice_list[1]:
    choice_list[1] += 1
option1 = choice_list[0]
option2 = choice_list[1]
count = 0
gameover = False


def check_answer(guess, followers1, followers2):
    if followers1 > followers2:
        return guess == "a"
    else:
        return guess == "b"


while not gameover:
    print(logo)
    print(f"Choice A: {option1['name']}, {option1['description']}, "
          f"from {option1['country']}.")
    print(vs)
    print(f"Choice B: {option2['name']}, {option2['description']}, "
          f"from {option2['country']}.\n")
    answer = input("Who has more followers? Type 'A' or 'B'. ")
    answer = answer.lower()
    followers1 = option1['follower_count']
    followers2 = option2['follower_count']
    if check_answer(answer, followers1, followers2):
        option1 = choice_list[1]
        choice_list[1] = random.choice(data)
        option2 = choice_list[1]
        count += 1
        if option1 == option2:
            index_value = data.index(option2)
            option2 = data[index_value - 1]
    else:
        print(f"Sorry, you are incorrect. Choice A has {followers1} million "
              f"followers and Choice B has {followers2} million followers.")
        gameover = True
        print(f"You made it {count} round(s).")