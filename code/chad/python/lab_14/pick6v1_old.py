import random

computer_picked = []
user_picked = []
wins = 0

def computer_choices(computer_picked):
    track_num = 1
    while track_num < 7:
        computer_pick = random.randint(0,100)
        computer_picked.append(computer_pick)
        track_num += 1
        if track_num == 7:
            return computer_picked

def user_choices(user_picked):
    track_num = 1
    while track_num < 7:
        user_pick = random.randint(0, 100)
        user_picked.append(user_pick)
        track_num += 1
        if track_num == 7:
            return user_picked

def ifwon(user_picked, computer_picked, wins):
    if computer_picked[0] == user_picked[0]:
        wins += 1
    if computer_picked[1] == user_picked[1]:
        wins += 1
    if computer_picked[2] == user_picked[2]:
        wins += 1
    if computer_picked[3] == user_picked[3]:
        wins += 1
    if computer_picked[4] == user_picked[4]:
        wins += 1
    if computer_picked[5] == user_picked[5]:
        wins += 1
    return wins


x = 0
won = 0
user_picked = (user_choices(user_picked))
computer_picked = (computer_choices(computer_picked))

while x < 1000:
    print(user_picked)
    print(computer_picked)
    won = (ifwon(user_picked, computer_picked, wins))
    print(won)
    x += 1

print(f'You Won {won} Times!!!')