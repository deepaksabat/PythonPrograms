#import random
n=input("enter guess number[1-10]:")
x=random.randint(1,10)
if n==x:
    print "wow your  guess is correct.You done great job"
else:
    print "sorry.Your guess is wrong.Better luck next time"
    
