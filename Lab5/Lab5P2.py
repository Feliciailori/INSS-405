def request():
    GenerateRandom()

import random as rand
def GenerateRandom():
    for n in range(1000):
        print(rand.randint(1,500))

request()

# Write a Python code to generate 1000 random numbers using a random function and print those random numbers. There is no restriction on range between random numbers; you can select your own range for this problem. You will need to create at least one function (one to generate a random number using the rand function) Don’t use return for the function where you try to generate random numbers; instead use the print statement. For example if I am generating 10 random numbers:
