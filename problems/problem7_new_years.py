"""
Start at 10 seconds and count down until 1 and then print "Happy New Year! 🎉"
"""
from time import sleep

x = 10
while x > 0:
    print(x)
    x = x-1
    sleep(1)
print('Happy New Year! 🎉')
