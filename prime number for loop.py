a=int(input("enter the number"))

c=0
for i in range(1,a+1):

    i=i+1
    if(a%i==0):
        c=c+i
if c==i:
    print("number is prime")
else:
    print("number is not prime")