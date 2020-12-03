import random

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

namecount = len(names)
roulette = random.randint(0, (namecount-1))

print(f"{names[roulette].upper()} has to pay the bill!")





