n = int(input())
n1 = 20
n2 = 21
print(n1, end=" ")
print(n2, end=" ")
for i in range(0, n):
    n3 = n1 + n2
    print(n3, end=" ")
    n1 = n2
    n2 = n3
