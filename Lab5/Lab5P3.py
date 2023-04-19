def request():
    num1=input('Enter number1=')
    num2=input('Enter number2=')
    num3=input('Enter number3=')
    print('Sum=',Addition(num1,num2,num3))
    print('Average=', Average(num1,num2,num3))
    print('Maximum=', Maximum(num1,num2,num3))
    print('Minimum=', Minimum(num1,num2,num3))
    print('Product=', Product(num1,num2,num3))

def Addition(num1,num2,num3):
    sum=int(num1)+int(num2)+int(num3)
    return sum

def Average(num1,num2,num3):
    ave=(int(num1)+int(num2)+int(num3)/3)
    return ave

def Maximum(num1,num2,num3):
    return max(num1,num2,num3)

def Minimum(num1,num2,num3):
    return min(num1,num2,num3)

def Product(num1,num2,num3):
    multiply=int(num1)*int(num2)*int(num3)
    return multiply

request()

# Write a Python code using functions to collect three numbers from users, and do the sum, average, max, min, and product of those numbers. You would need to have function for each operation and one function for input.  For example here is how your code should work:
# Input number 1: 10
# Input number 2 :20
# Input number 3: 30
# Sum= 60
# average= 20
# max= 30
# min=10
# product=600
