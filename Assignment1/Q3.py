sum=0
for x in range(14):
    score=input('Enter Score=')
    if(int(score)>=90):
        print('A')
    elif(int(score)>=80 and int(score)<=89):
        print('B')
    elif(int(score)>=75 and int(score)<=79):
        print('C')
    elif(int(score)>=60 and int(score)<=74):
        print('D')
    elif(int(score)<=59):
        print('F')
    sum=sum+int(score)
print('Final Sum=',sum)
average=int(sum)/14
print('Average=',average)

#final scores for 14 courses between 2021 and 2022. Calculate total sum and average

# else:
#     print('F')