number=input('Enter Number:')
if(int(number)%3==0 and int(number)%5!=0 and int(number)%15!=0):
    print('Bowie')
elif(int(number)%5==0 and int(number)%3!=0 and int(number)%15!=0):
    print('Bowie State')
elif(int(number)%15==0):
    print('Bowie State University')