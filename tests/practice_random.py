import random

number = random.randint(1,100)

print(number)

chance = random.random()

if chance < 0.3:
    print("Critical Hit!")
else:
    print("Normal attack")