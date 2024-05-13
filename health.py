import random

health = 50

user_input = int(input("Choose Difficulty: "))

if user_input > 3:
    raise ValueError("Input must not be greater than 3")
elif user_input < 0:
    raise ValueError("Input must not be less than 0")

#Highest difficulty is 3
#difficulty = 1
    

potion_health = int(random.randint(25,50) / user_input)

health = health + potion_health

print(health)
