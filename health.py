import random

health = 50

while True:
    try:
        user_input = int(input("Choose Difficulty (1-3): "))

        if user_input > 3:
            raise ValueError("Input must not be greater than 3")

        elif user_input < 1:
            raise ValueError("Input must not be less than 0")
        break
    except ValueError as e:
        print(e)    
#Highest difficulty is 3
#difficulty = 1
    

potion_health = int(random.randint(25,50) / user_input)

health = health + potion_health

print(health)
