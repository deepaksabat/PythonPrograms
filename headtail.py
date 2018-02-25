import random
i=1
hcnt=0
tcnt=0
while i<=50:
    n=random.randint(0,1)
if n==0:
    hcnt+=1
elif n==1:
    tcnt+=1
    i+=1
print"No of heads turned:",hcnt
print"No.of trails  turned",tcnt
