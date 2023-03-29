#i is the loop variable. it can be replaced with any letter

# print('0')
# print('1')
# print('2')
# print('3')
# print('4')
# for i in range(5):
#     print(i)

#for even number range. Expected outcome is 5 numbers, 0,2,4,6,8
# for i in range(10):
#     if(i%2==0):
#         print(i)

#for odd number range. exepected outcome is 5 number, 1,3,5,7,9
# for i in range(10):
#     if(i%2!=0):
#         print(i)

#the above is needed for when you want to collect random input from users
# for i in range(5):
#     number=input('Enter a number')
#     print(number)

#classwork
# for i in range(100):
#     print(i)

# for i in range(100):
#     if(i%2==0):
#         print(i)
#
# for x in range(100):
#     if(x%2!=0):
#         print(x)

# for x in range(1,10):
#     print(x)

# for x in range(5,10):
#     print(x)

# for x in range(5,10,2):
#     print(x)
#5=where the range starts from, 10=range,2=incremental value from range start (5)

#for random numbering within a range. Next line can also be left alone as random without an alias rand
# import random as rand
# print(rand.randint(1, 100))
# #a random number within a range of 1-100
#
# import random as rand
# for x in range(10):
#     print(rand.randint(1,100))
#10 random numbers from 1 to 100

# import random as rand
# print(rand.randint(500,600))
#a random number from 500 within a range of 600

# import random as rand
# for x in range(30):
#     print(rand.randint(1,500))

# import random as rand
# sum=0.00
# for x in range(30):
#     print('x=',x)
#     print(rand.randint(1,500))
#     sum=sum+rand.randint(1,500)
#     print('sum=',sum)
# print('final sum=',sum)

import random as rand
sum=0.00
for x in range(30):
    print('x=',x)
    print(rand.randint(1,500))
    sum=sum+rand.randint(1,500)
    print('sum=',sum)
print('final sum=',sum)
average=sum/30
print('Average=',average)
