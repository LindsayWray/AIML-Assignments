"""
Build a dictionary of universal constants and use them to build a calculator in any
two of the applications that access constant values from dictionary.
example: pi = 3.14
radius as input
area of circle = pi*r*r
"""

my_dict = {"pi":3.14, "c": 3e8}
radius = int(input("Enter the radius: "))
print(f"the area of the circle is: {my_dict['pi'] * radius * radius}")

mass = int(input("Enter the mass: "))
print(f"the energy is: {mass * my_dict['c']**2}")