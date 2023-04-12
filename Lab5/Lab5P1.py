def request():
    num=input('Enter Variable num')
    print(even(num))



def even(num):
    if(int(num)%2==0):
        return 'Even number'
    else:
        return 'Odd number'

request()

# Write a Python code to collect input from the user and determine if the given number is odd or even. You are required to use functions, if your code doesn’t have functions you will receive no credit for this problem.If you have functions for odd/even, please make sure that you check one of them and use that output to determine if you need to call the other function. For example your input number is 4, and you first check for even if it is true you can skip the odd function as it is evident that it is an even number. [Hint: You would need just two functions input and even/odd function (only one of them) which will tell you if it is odd or even]
# Example input: 4
# Your output should print  ”Even number” (without quotes)
# Example input: 5
# Your output should print  ”Odd number” (without quotes)
