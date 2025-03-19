# Assignments on functions

# Write a program to create a function that takes two arguments, name and age, and print their value.
def display_info(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

display_info("Harish", 26)

# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call
def calucalations(a,b):
    addition= a+b
    subtraction= a-b
    return addition, subtraction

a=59
b=35

print(f"Addition: {a+b}")
print(f"Subtraction: {a-b}")

# Write a program to create a function show_employee() using the following conditions.
# ●  	It should accept the employee’s name and salary and display both.
# ●  	If the salary is missing in the function call then assign default value 9000 to salary
def display_employee(name, salary=9000):
    print(f"Employee Name: {name}")
    print(f"Salary: {salary}")
    
display_employee("Smith", 78000)
display_employee("Mike")
    
# 4.	Accept a number from the user, create a function isPrime(), which accepts a number from a parameter & check prime or not. If number is prime return True & number else return false & number
     
def is_prime(num):
    if num < 2:
        return False, num
    for i in range(2, num):
        if num % i == 0:
            return False, num
    return True, num
    
num = int(input("Enter a number: "))
result, value = is_prime(num)
print(f"Is {value} a prime number? {result}")

# 5.	Create menu driven calculation (add,sub,multiply, divide, mod) using function
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

a=int(input('Enter a number :'))
b=int(input('Enter a number :'))

print('1. Addition')
print('2. Subtraction')
print('3. Multiply')
print('4. Divide')
print('5. Modulus')
op=int(input('Select any one number from above'))

if op==1:
    result=add(a,b)
    print(f'addition is {result}')
elif op==2:
    result=sub(a,b)
    print(f'subtracgtion is {result}')
elif op==3:
    result=mul(a,b)
    print(f'multiplication is {result}')
elif op==4:
    result=div(a,b)
    print(f'division is {result}')
elif op==4:
    result=mod(a,b)
    print(f'modulus is {result}')
else:
    print('You have not selected number from 1-5')

 
# 6.	Create a function to accept a number & return its factorial
num= int(input("Enter a number: "))
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(f"Factorial of {num} is: {factorial(num)}")

# 7.	Create a function that accept student data, calculate the total & percentage, return total & percentage
def calculate_result(marks):
    total = sum(marks)  
    percentage = (total / (len(marks) * 100)) * 100 
    return total, percentage

marks = [80, 90, 75, 85, 95]  
total, percentage = calculate_result(marks)
print("Total Marks:", total)
print("Percentage:", percentage, "%")

# 8.	Create a login function, that accept username & password, if username is ‘admin’ & password is ‘admin@123’ then return true, else return false
def login(username, password):
    return username == "admin01" and password == "admin@123"

user = input("Enter username: ")
pwd = input("Enter password: ")

if login(user, pwd):
    print("Login Successful")
else:
    print("Invalid Username or Password")
    
# 9.	Create a function to generate fibonacci series  like  0, 1, 1, 2, 3 5
def fibonacci(n):
    a, b = 0, 1 
    fib_series = [] 
        
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b 
        
    return fib_series

num= int(input("Enter the number of terms: "))
print("Fibonacci Series:", fibonacci(num))
        
# 10.   Create a function which accept a string & character, check the occurrence of given character in a string and return the count
def count_character(string, char):
    return string.count(char) 

text = input("Enter a string: ")
character = input("Enter the character to count: ")
print(f"'{character}' appears {count_character(text, character)} times in the string.")
