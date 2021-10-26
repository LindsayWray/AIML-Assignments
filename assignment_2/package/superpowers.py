food_dict = {
"candy": {"books": " time traveling", "movies": "n elastic"},
"vegetables": {"books": " healing powered", "movies": "n immortal"},
"carbs": {"books": " shapeshifting", "movies": " force field yielding"},
"coffee": {"books": " mind controlling", "movies": " X-ray visioned"},
"nuts": {"books": " telekineting", "movies": "n invisible"}
}

def which_superpower(food, media):
	media_dict = food_dict[food]
	superpower = media_dict[media]
	return superpower