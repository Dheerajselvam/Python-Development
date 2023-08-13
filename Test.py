v1= int(input('Enter number 1: '))
v2= int(input('Enter number 2: '))
op= input('Enter operation (+, -, *, /): ')

if op == '+':
    x = v1+v2
elif op=='-':
    x = v1-v2
elif op=='*':
    x = v1*v2
elif op=='/':
    x = v1/v2 
else:
    print('Enter Valid Operation')
    exit()

print("The Answer is : ", x)