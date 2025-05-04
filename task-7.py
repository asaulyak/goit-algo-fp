import random

def roll_dices():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)

    return dice_1 + dice_2


tries = 1500000
result = []
for i in range(tries):
    result.append(roll_dices())


stats = {dice + 2: '{:.2%}'.format(result.count(dice + 2) / tries) for dice in range(11)}


print(stats)
