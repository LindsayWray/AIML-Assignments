food_dict = {
"🍭 Candy": {"📚 Books": " time traveling", "🎬 Movies": "n elastic"},
"🥦 Vegetables": {"📚 Books": " healing powered", "🎬 Movies": "n immortal"},
"🍝 Carbs": {"📚 Books": " shapeshifting", "🎬 Movies": " force field yielding"},
"☕️ Coffee": {"📚 Books": " mind controlling", "🎬 Movies": " X-ray visioned"},
"🌰 Nuts": {"📚 Books": " telekineting", "🎬 Movies": "n invisible"}
}

def which_superpower(food, media):
	media_dict = food_dict[food]
	superpower = media_dict[media]
	return superpower