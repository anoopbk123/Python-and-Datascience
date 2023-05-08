with open('hello.txt','a') as file:
    file.write('hello 3')
with open('hello.txt', 'r') as file:
    print(file.read())