def request():
    score1 = float(input("Enter Score:"))
    score2 = float(input("Enter Score:"))
    score3 = float(input("Enter Score:"))
    score4 = float(input("Enter Score:"))
    sum=float(score1)+float(score2)+float(score3)+float(score4)
    mean=sum/4
    print ("Mean Score: ", mean)
    (grades(mean, score1,score2,score3,score4))
def grades(mean, score1,score2,score3,score4):
    if float(mean)>=90:
        print ("Grade: A")
    elif float(mean)>=80 and float(mean)<90:
        print ("Grade: B")
    elif float(mean)>=70 and float(mean)<80:
        print ("Grade: C")
    elif float(mean)>=60 and float(mean)<70:
        print ("Grade: D")
    elif float(mean)>=50 and float(mean)<60:
        print("Grade: E")
    elif float(mean)<50:
        print("Grade: F")


request()