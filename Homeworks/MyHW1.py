#Explain your work
#Generating a 3*3 matrix with 9 random prime numbers.(with #using the for loop)

#***random numbers are generated between 0-50*****
#Question 1
from random import randint
for i in range(3):
    for j in range(3):
        control = False
        while control is False:
            num = randint(0,50)
            
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    control=True
                        
        print(num, end=" ")
    print("\n")
