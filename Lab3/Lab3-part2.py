score1=input('Enter Score for INS405')
score2=input('Enter Score for BUIS 360')
score3=input('Enter Score for DANL 470')

print(type('score'))

Sum=int(score1)+int(score2)+int(score3)
print('Sum', Sum)
Average=(int(score1)+int(score2)+int(score3))/3
print('Average', Average)

if(int(Average)>90):
    print('A')
if(int(Average)<=89 and int(Average)>=70):
    print('B')
if(int(Average)<=69 and int(Average)>=60):
    print('C')
if(int(Average)<59):
    print('F')




