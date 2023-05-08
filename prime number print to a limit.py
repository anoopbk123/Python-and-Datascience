n=int(input('enter limit'))
for i in range(1,n):
    f=0
    for j in range(2,i//2):
        if i%j==0:
            f=1
            break
    if i==4:
        pass
    elif f==0:
        print(i)
