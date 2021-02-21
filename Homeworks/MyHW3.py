#Explain your work
#write two functions, these two functions must be used
#inside the loop (values between 0-1000) press the prime
#numbers between 0-500 on the screen with the prime_first
#function and press the prime numbers between 500-1000 on
#the screen with the prime_second function
#Question 1
def prime_first(i):
    if i >1:
        for j in range (2,i):
            if(i%j)==0:
                break
        else:
            print(i, end="\n")

def prime_second(i):
    if i >1:
        for j in range (2,i):
            if(i%j)==0:
                break
        else:
            print(i, end="\n")
            
print("************PRİME FİRST************")            
for i in range(0,1000):
    if(i<500):
        prime_first(i)
    elif(i==500):
        print("************PRİME SECOND************")
    else:
        prime_second(i)
