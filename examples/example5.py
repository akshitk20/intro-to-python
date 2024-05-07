def add(a, b):
    return a + b


def say_hello(name, shout=False):  # optional argument shout
    greeting = 'Hello ' + name
    if shout:
        greeting = greeting.upper()
    return greeting


print(say_hello('beyoncé'))
print(say_hello('beyoncé', True))   # positional and positional
print(say_hello('beyoncé', shout=False))  # positional and keyword argument
print(say_hello(name='beyoncé', shout=True))  # keyword arguments