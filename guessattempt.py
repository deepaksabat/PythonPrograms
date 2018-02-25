import random
x=random.randint(1,100)
i=1
while i<=5: 
    a=input("enter a guess number[1 To 20]:")
    break

if a==x:
    print"wow your guess is correct.You guessed by number in",i,"attempts"

elif a>x:
    print"your guess is high"
    i+=1
else:
    print"yout attempts are over.Better next time "
    

