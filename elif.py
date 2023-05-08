gender = str(input("enter your gender")).lower()
if gender == 'female' or gender == 'f':
    print('welcome lady')
elif gender == 'other' or gender == 'o':
    print('welcome')
elif gender == 'male' or gender == 'm':
    print("welcome guys")
else:
    print('enter correct answer')
