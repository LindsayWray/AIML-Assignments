element_dict = {
"earth": {"morning": "giraff 🦒", "afternoon": "elephant 🐘", "night": "cat 🐈"},
"water": {"morning": "turtle 🐢", "afternoon": "hippopotamus 🦛", "night": "shark 🦈"},
"fire": {"morning": "ant 🐜", "afternoon": "dragon 🐉", "night": "cockroach 💥"},
"air": {"morning": "eagle 🦅", "afternoon": "butterfly 🦋", "night": "bat 🦇"}
}

def which_animal(element, daytime):
	daytime_dict = element_dict[element]
	animal = daytime_dict[daytime]
	return animal
