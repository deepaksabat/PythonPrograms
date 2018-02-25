r=input("enter no. of rows:")
c=input("enter no.of  columns:")
i=1
if r==c:
    c=c-1
    while i<=r:
        print"---|"*c+"---"
        i+=1
else:
    print"sorry rows and columns are not  equal"
