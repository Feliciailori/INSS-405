import random as rand
sum=0.00
for i in range(1000):
    print(rand.randint(1, 1000))
    sum=sum+rand.randint(1,1000)
print("final sum", sum)
average=sum/1000
print("Average", average)

#Using For loop discussed in the previous class and generate 1000 random numbers using rand function and print out their sum and average.


