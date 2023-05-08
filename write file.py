c=1
while c > 0:
   with open("hello.txt", 'a') as file:
        line=str(input('enter the line'))
        file.writelines(str(line)+'\n')
   c=int(input('for entter another line press 1 \n to exit press 0'))
print('the file after input')
with open('hello.txt','r') as f:
    print(f.read())