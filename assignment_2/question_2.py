from package import animals
from package import superpowers

print("\nTake this quiz, and find out which superpowered animal you are!\n")

while True:
	query_1 = input("Pick your favourite element:\nEarth ⛰\nWater 🌊\nFire 🔥\nAir 🌪\n").lower()
	if query_1 in animals.element_dict:
		break
	else:
		print("\nNot a valid option, try again!\n")
while True:
	query_2 = input("Pick your favourite time of the day:\nMorning 🌅\nAfternoon 🌞\nNight 🌚\n").lower()
	if query_2 in animals.element_dict[query_1]:
		break
	else:
		print("\nNot a valid option, try again!\n")
while True:
	query_3 = input("Pick a type of food:\nCandy 🍭\nVegetables 🥦\nCarbs 🍝\nCoffee ☕️\nNuts 🌰\n").lower()
	if query_3 in superpowers.food_dict:
		break
	else:
		print("\nNot a valid option, try again!\n")
while True:
	query_4 = input("Do you prefer books or movies?\n").lower()
	if query_4 in superpowers.food_dict[query_3]:
		break
	else:
		print("\nNot a valid option, try again!\n")

animal = animals.which_animal(query_1, query_2)
superpower = superpowers.which_superpower(query_3, query_4)
print(f"\nThe results are in 🥁:\n\nYou are a{superpower} {animal}!\n")