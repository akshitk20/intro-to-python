"""
Calculate the gravitational force between Earth and Venus
"""

G = 6.67e-11  # Gravitational constant

mass_1 = 6e24  # in kg (mass of Earth)
mass_2 = 4.9e24  # in kg (mass of Venus)
distance = 4.1e10  # in m (distance between Earth and Venus)

#force = None  # <-- Replace with your code
radius = distance / 2
force = (G * mass_1 * mass_2) / distance ** 2  # <-- distance * distance = distance raised to 2
print(force)

# escape character \ \n
# math
#  distance * distance = distance raised to 2 = distance ** 2
# python3 test.py
# none = null
# no camel casing like java use _
# insinstance() to check the type of object
# name = input("What's your name?")
# bool([]) = false
# capitialize to make first letter as captial
# title same as above
# use {} for string concatenation print(f"Temp in C: {round(temp_c)}")
# random random.randint(1, 6) include 1 and 6
# pypi.org
# if there is no return value then return is NONE
#print(say_hello('beyoncé'))
#print(say_hello('beyoncé', True))   # positional and positional
# print(say_hello('beyoncé', shout=False))  # positional and keyword argument
# print(say_hello(name='beyoncé', shout=True))  # keyword arguments
# string[-1] -> last letter in string
# string[0:4] not including 4
# print(string[::2]) skip 2 characters
# print(string[::-1]) reverse the string
# in -> to check if something is inside string or list
