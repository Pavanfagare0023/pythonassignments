# # 1. WAP to print even numbers from 121 to 229 using for loop.
n1 =121
while n1<=229:
    if n1%2==0:
        print(n1, end='')
    n1+=1


  
# # 2. WAP to print odd numbers from 521 to 229 using while loop.
n2=521
while n2>=229:
    if n2%2!=0:
        print(n2, end='')
    n2-=1


# # 3. Write a Python program to print all alphabets from a to z using for loop
ch =90
while ch<=120:
    print(chr(ch), end=" ")    
    ch+=1

    
    
# # 4. Write a Python program to find the sum of all even numbers between 1 to n.
n3= int(input("Enter the value of n: "))
sum_even = 0
num=2
while num<=n3:
    sum_even += num
    num+=2
print("Sum of even numbers:", sum_even)
            
        
# # 5. Write a Python program to find the sum of all odd numbers between 1 to n.
n4= int(input("Enter the value of n: "))
sum_odd = 0
num=1
while num<=n4:
    sum_odd += num
    num+=2
print("Sum of odd numbers:", sum_odd)
 

# # 6. Write a Python program to count number of digits in any number
n5=int(input('Enter a number :'))
count=len(str(abs(n5)))
print('Number of digit :', count)


# # 7. WAP to print table of given no
n6=int(input('Enter a number :'))
i =1
while i<=10:
    print(f'{n6}*{i}={n6*1}')
    i+=1


# # 8. WAP to print squares from 1 to20
n7=1
while n7<=20:
    print(f'Square of {n7} ={n7**2}')
    n7+=1
   
    

# 9. WAP to check given no is palindrome or not. Original =Reverse
# Eg 1221
n8=int(input('Enter a number:'))
rev=0
while n8>0:
    digit=n8%10
    rev=rev*10+digit
if n8 == rev:
    print('{n8} is a palindrome')
    
    
    
# 10.  Accept the number & check number is prime number or not (number divide by 1 & itself)
num=int(input('Enter a number :'))
i=2
temp=0
    while i<num:
         if(n%i==0):
        temp=1
        i+=1
    if temp==0:
        print('{num} is prime number')
    else:
            print('{num} is not prime number')

num=int(input('Enter a number :'))
sum=0
temp=num

# 11.  Accept the number & check number is Armstrong number
num=int(input('Enter a number :'))
temp=num
sum=0
while num!=0:
    sum=sum+(r*r*r)
    num//=10
    
    if temp==num:
        print('Armstrong Number', sum)
    else:
        print('Not a Armstrong Number')
 
