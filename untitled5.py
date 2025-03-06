# 3. Write a Python program to enter length and breadth of a rectangle and find its Area

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

area = length * breadth

print(f"Area of the rectangle: {area}")


# 4. Write a Python program to enter base and height of a triangle and find its area..

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = 0.5 * base * height

print(f"Area of the triangle: {area}")

# 5. Write a python Program to calculate Square of given number

num = float(input("Enter a number :"))

square=num**2

print(f"square of {num} is {square}")

# 6. Write a python Program to calculate cube of given number

num = float(input("Enter a number :"))

cube=num**2

print(f"cube of {num} is {cube}")

# 7. Write a Python program to enter marks of five subjects and calculate total, average

sub1=float(input('Enter marks for subject1:'))
sub2=float(input('Enter marks for subject2:'))
sub3=float(input('Enter marks for subject3:'))
sub4=float(input('Enter marks for subject4:'))
sub5=float(input('Enter marks for subject5:'))

total=sub1+sub2+sub3+sub4+sub5
avaerage=total/5
percentage=(total/500)*100

print(f'Total marks:{total}')
print(f'Avarage marks:{avaerage}')
print(f'Percentage marks:{percentage}')

# 8. Write a Python program to enter P, T, R and calculate Simple Interest.

P=float(input('Enter principal amount :'))
T=float(input('Enter time in year :'))
R=float(input('Enter rate of interest per annum :'))

SI=(P*T*R)/100

print(f'simple interest: {SI}')

# 10. Write a program to accept 2 number and find greatest

num1=float(input('Enter first number :'))
num2=float(input('Enter second number :'))

if num1>num2:
    print(f'Greatest number is {num1}')
elif num2>num1:
    print(f'Greatest number is {num2}')
else:
    print('Both are equal')
       