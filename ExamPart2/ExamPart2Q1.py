def request():
    numbers = []
    for i in range(11):
        number= float(input("Enter number:"))
        numbers.append(number)

    print ("SUM:", calculatesum(numbers))
    print ("MEAN:", calculatemean(numbers))
    print ("MEDIAN:", calculatemedian(numbers))

def calculatesum(numbers):
    totalsum=sum(numbers)
    return totalsum

def calculatemean(numbers):
    mean=sum(numbers)/len(numbers)
    return mean

def calculatemedian(numbers):
    #because len(numbers)%2 != 0
    middle = len(numbers)//2
    median = sorted(numbers)[middle]
    return median

request()

