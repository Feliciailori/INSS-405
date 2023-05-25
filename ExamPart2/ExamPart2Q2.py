import random as rand
def request():
    numbers = []
    for n in range(100):
        number=rand.randint(1,100)
        numbers.append(number)
    print("Sorted Numbers:", sorting(numbers))
def sorting(numbers):
    sortednum= sorted(numbers)
    return sortednum

request()