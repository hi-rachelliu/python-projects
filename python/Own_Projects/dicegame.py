import random

roll_dice = input( "Do you want to roll a dice?")
if roll_dice == "Yes" or "Y":
    dice = random.randint(1, 6)
    print (dice)


