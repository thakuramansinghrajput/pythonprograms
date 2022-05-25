a=int(input("enter the height"))
l=int(input("middle line position"))
k=0
for i in range(1,a+1):
    for j in range(a-i):
        print(" ",end='')
    while 2*i-l>k:
        if k==0 or k==2*i-2 or i==l:
            print("*",end="")
        else:
            print(" ",end='')
        k+=1
    print()
    k=0