def printmax(a,b):
    if a>b:
        #print(a)
        c=a
        return c
    elif a ==b :
        print('a=b')
    else :
        c=b
        return c
        #print(b)

a=input("enter a number")
b=input("enter a number")
c=printmax(a,b)
print(c)