import random as rand

def request():
    for i in range(100):
        num=(rand.randint(1,100))
        (oddnumbers(num))

def oddnumbers(num):
    if int(num)%2 != 0:
        print ("Random Odd number:", num)

request()