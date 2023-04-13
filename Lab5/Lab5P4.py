def request():
    num=input('Enter Temperature')
    print (hottemperature(num))

def hottemperature(num):
    if (int(num)<=30):
        return 'Cold'
    elif (int(num)>=31 and int(num)<=40):
        return 'Warm'
    elif (int(num)>=50):
        return 'Hot'



request()

# Write a python code using functions to collect input temperature from user and determine if it is hot / cold / warm.
# Your code should have atleast 3 functions one for input, second to determine if it is hot / cold / warm,
# and third to print the output.Please use the below table to determine the hot / cold / warm.
