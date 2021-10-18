element_dict = {
"⛰ Earth": {"🌅 Morning": "giraff 🦒", "🌞 Afternoon": "elephant 🐘", "🌚 Night": "cat 🐈"},
"🌊 Water": {"🌅 Morning": "turtle 🐢", "🌞 Afternoon": "hippopotamus 🦛", "🌚 Night": "shark 🦈"},
"🔥 Fire": {"🌅 Morning": "ant 🐜", "🌞 Afternoon": "dragon 🐉", "🌚 Night": "cockroach 💥"},
"🌪 Air": {"🌅 Morning": "eagle 🦅", "🌞 Afternoon": "butterfly 🦋", "🌚 Night": "bat 🦇"}
}

def which_animal(element, daytime):
	daytime_dict = element_dict[element]
	animal = daytime_dict[daytime]
	return animal
