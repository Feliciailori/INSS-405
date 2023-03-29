for i in range (7):
    temperature=input('Enter Temperature:')
    if(float(temperature)>=50):
        print("Hot")
    elif(float(temperature)>=30 and float(temperature)<50):
        print("Warm")
    elif(float(temperature)>=0 and float(temperature)<30):
        print("Cold")
    elif(float(temperature)<0):
        print("Extreme Cold")

#Write a program using for loop which accepts temperature as input  from user and
# determines the categories listed below.  The user may enter temperature n times
# where n is any random number whichever you like.
# [You would need to use if/else along with for loop
