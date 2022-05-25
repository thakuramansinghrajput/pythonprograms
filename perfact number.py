a=int(input("enter the number"))
i=0
s=0
while(i<a-1):
    i=i+1
    if a%i==0:
        s=s+i
if(s==a):
    print("yes it is perfact number")
else:
    print("no it is not a perfact number")
