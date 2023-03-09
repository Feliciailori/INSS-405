score1=input('Enter Score for INS405')
score2=input('Enter Score for BUIS 360')
score3=input('Enter Score for DANL 470')

print(type('score'))

Sum=float(score1)+float(score2)+float(score3)
print('Sum', Sum)
Average=(float(score1)+float(score2)+float(score3))/3
print('Average', Average)

#Grade>90=A
#Grade70-89=B
#Grade60-69=C
#Grade<59=F

if(float(Average)>90):
    print('A')
if(float(Average)<=89 and float(Average)>=70):
    print('B')
if(float(Average)<=69 and float(Average)>=60):
    print('C')
if(float(Average)<=59):
    print('F')




