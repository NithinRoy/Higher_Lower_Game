import art
import game_data
import random
import os

random_number1 = random.randint(0,49)
random_number2 = random.randint(0,49)
if random_number1 == random_number2:
    random_number2 = random.randint(0,49)

def person1(random_number1):
    name = game_data.data[random_number1]['name']
    follower_count1 = game_data.data[random_number1]['follower_count']
    description = game_data.data[random_number1]['description']
    country = game_data.data[random_number1]['country']
    print(art.logo)
    print(f"Compare A: {name}, a {description}, from {country}")
    return follower_count1

def person2(random_number2):
    name = game_data.data[random_number2]['name']
    follower_count2 = game_data.data[random_number2]['follower_count']
    description = game_data.data[random_number2]['description']
    country = game_data.data[random_number2]['country']
    print(art.vs)
    print(f"Against B: {name}, a {description}, from {country}")
    return follower_count2

stop = True
score = 0
while stop:
    count1 = person1(random_number1)
    count2 = person2(random_number2)
    highest = input("Who has more followers? Type 'A' or 'B': ")
    if highest == 'A':
        if count1 > count2:
            score += 1
            random_number2 = random.randint(0,49)
            if random_number1 == random_number2:
                random_number2 = random.randint(0,49)
            os.system('cls')
        else:
             print(f"Sorry. You have lost. Score = {score}")
             stop = False
    elif highest == 'B':
        if count1 < count2:
            score += 1
            random_number1 = random_number2
            random_number2 = random.randint(0,49)
            if random_number1 == random_number2:
                random_number2 = random.randint(0,49)
            os.system('cls')
        else:
             print(f"Sorry. You have lost. Score = {score}")
             stop = False