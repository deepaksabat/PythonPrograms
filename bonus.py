# Write a scrpt accept empno,ename,job and salary and
#calculate bonus
#based on the following condtions

#job       bonus
#manager    20% on ann_sal
#analyst    18% on ann_sal
#programmer 15% on ann_sal
#salesman   12% on ann_sal
#others     10% on ann_sal

empno=input("Enter a  empno : ")
ename=raw_input("Enter a ename : ")
job=raw_input("Enter a job : ")
sal=input("Enter a salary : ")

ann_sal=sal*12

if job=="manager" :
    bonus=ann_sal*20/100
elif job=="analyst" :
    bonus=ann_sal*18/100
elif job=="programmer" :
    bonus=ann_sal*15/100
elif job=="salesman" :
    bonus=ann_sal*12/100
else :
    bonus=ann_sal*10/100

print "#"   *  40
print "###   Employee Bonus Report  ####"
print "-" * 40
print "###   Employee Number  : ",empno, " ###"
print "###   Employee Name    : ",ename, " ###"
print "###   Employee Job     : ",job, " ###"
print "###   Employee Salary  : ",sal, " ###"
print "###   Employee AnnSal  : ",ann_sal, " ###"
print "###   Employee Bonus   : ",bonus, " ###"
print "-" * 40
print "#"   *  40
