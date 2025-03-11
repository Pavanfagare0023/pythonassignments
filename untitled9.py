# WAP to print even numbers from 121 to 229 using for loop.
for num in range(122, 230, 2): 
    print(num, end=" ")

# WAP to print odd numbers from 521 to 229 using a for loop.
for num in range(521, 228, -2):  
    print(num, end=" ")


# Write a Python program to print all alphabets from a to z using for loop
for char in range(97, 123):  
    print(chr(char), end=" ")

# Write a Python program to find the sum of all even numbers between 1 to n.
n = int(input("Enter a number: "))
sum_even = 0
for num in range(2, n + 1, 2):
    sum_even += num
print("Sum of even numbers:", sum_even)


# Write a Python program to find the sum of all odd numbers between 1 to n.
n = int(input("Enter a number: "))
sum_odd = 0
for num in range(1, n + 1, 2):
    sum_odd += num
print("Sum of odd numbers:", sum_odd)




