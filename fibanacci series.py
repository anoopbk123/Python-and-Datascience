n=int(input('enter a number'))
n1=0
n2=1
print(n1,end='\t')
print(n2,end='\t')
for i in range(0,n):
    n3=n1+n2
    print(n3,end='\t')
    n1=n2
    n2=n3
