#Homework: 
#Get 20 random marks for 20 students (between 0 to 100). Create 3 separate lists . The first list should contain the marks <=30
#The second list between 31 to 69. The third list >= 70. Display the output lists
#(random.randint)

import numpy as np
import random

start = int(input("enter a starting range for marks : "))
end = int(input("enter ending range for marks : "))
num = 20

def Rand(start, end, num):
    marks = []
 
    for j in range(num):
        marks.append(np.random.randint(start, end))
 
    return marks
list1 = Rand(start, end, num)
print(list1)

type1 = []
type2 = []
type3 = []

for catagories in list1:
    if catagories <= 30:
        type1.append(catagories)
        #print("you failed")

    elif 31<=catagories<=69:
        type2.append(catagories)
        #print("you passed")

    else:
        type3.append(catagories)
        #print("you passed with flying colours")


print("Marks of students who failed are : ", type1)
print("Marks of students who passed are : ", type2)
print("Marks of students who passed with very good marks  are : ", type3)








