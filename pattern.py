n=int(input("enter the number of rows"))

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end='')
    print("*",end='')
    for j in range(2,i+1):
        print(" ",end='')
    for j in range(2,i+1):
        print(" ",end='')
    print("*",end='')
    print()
