def convert_temperature(celcius):
	kelvin = celcius + 273.15
	fahrenheit = (celcius * 1.8) + 32
	print(f"{celcius} degrees celcius is {fahrenheit} degrees Fahrenheit and {kelvin} Kelvin")

celcius = int(input("Enter a temperature in degrees Celcius "))
convert_temperature(celcius)