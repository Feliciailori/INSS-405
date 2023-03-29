number=input('Enter Number:')
if(int(number)%3==0 and int(number)%5!=0 and int(number)%15!=0):
    print('Bowie')
elif(int(number)%5==0 and int(number)%3!=0 and int(number)%15!=0):
    print('Bowie State')
elif(int(number)%15==0):
    print('Bowie State University')

#another method is to put the syntax from bottom to top. That is start with 15 instead of 5
# if(int(number)%15==0)
#     print('Bowie State University')
# if(int(number)%5==0)
#     print('Bowie State')
# if(int(number)%3==0):
#     print('Bowie')