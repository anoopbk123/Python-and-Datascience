n=int(input('enter the number of rows'))
for i in range(1,n):
    for j in range(0,i):
        #end must be defind or it will print in next line
        print('*',end="_")
    print()