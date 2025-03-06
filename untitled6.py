  
# 11. WAP to accept 3 numbers & print the greatest
   
num1=float(input('Enter first number :'))
num2=float(input('Enter second number :'))
num3=float(input('Enter third number :'))

if num1>=num2 and num1>=num3:
    print(f'Greatest number is {num1}')
elif num2>=num1 and num2>=num3:
    print(f'Greatest number is {num2}')
else:
    print(f'Greatest number is {num3}')
    

# 9. Swap values of two integer variables.

a=float(input('Enter a first number :'))
b=float(input('Enter a second number :'))

a,b = b,a

print(f'After swapping : fisrt number ={a}, second number ={b}')