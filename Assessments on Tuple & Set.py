# Assessments on Tuple & Set
# 1. Write a Python program to create a tuple.
t1=(12,45,86,90,23)
print(t1)

# 2. Write a Python program to create a tuple with different data types
t2=(2,"Hello, Mumbai", 12.9,[1,8,9,6])
print(t2)

# 3. Write a Python program to create a tuple with numbers and print one item.
t3=(20,80,90,60,50,40)
print(t3[5])

# 4. Write a Python program to unpack a tuple in several variables.
t4= (29,34,56)
x,y,z=t4
print(x,y,z)

# 5. Write a Python program to add an item in a tuple.
t5=(20,80,90,60,50,40)
t5=t5+(26,62,)
print(t5)

# 6. Write a Python program to convert a tuple to a string.
t6=("G","O","O","D" ,"M","O","R","N","I","N","G")
str="".join(t6)
print(str)


# 7. Write a Python program to get the 4th element and 4th element from last of a tuple.
t7= (2,12,80,90,60,55,69,52,63,42,90,50)
print(t7[4])
print(t7[-4])


# 8. Write a Python program to reverse a tuple.
t8=(10,20,30,40,50,60,70,)
print(t8[::-1])


# 9. Write a Python program to find the repeated items of a tuple.
# 10. Write a Python program to check whether an element exists within a tuple.
t9=(20,80,90,60,50,40,20,90,10,60,80,90)

print(t9.count(60)) #find the repeated items of a tupl

print(20 in t9) #check whether an element exists within a tuple


# 11. Write a Python program to convert a list to a tuple.
l=[1,8,9,6,7,5,3,2]
t=tuple(l)
print(t)

# 12. Write a Python program to remove an item from a tuple.
# 13. Write a Python program to slice a tuple.
# 14. Write a Python program to find the index of an item of a tuple.
# 15. Write a Python program to find the length of a tuple.

t10=(40,20,90,10,60,80,90)
t10=tuple(i for i in t10 if i!=60) #remove an item from a tuple

print(t10)

print(t10[20:10]) # slice a tuple

print(t10.index(90)) #find the index of an item of a tuple

print(len(t10)) #find the length of a tuple


# 16. Write a Python program to sort list of tuple based on sum
# Input: [(4, 5), (2, 3), (6, 7), (2, 8)]
# Output: [(2, 3), (4, 5), (2, 8), (6, 7)]"

l1=[(4,5),(2,3),(6,7),(2,8)]
n=len(l1)
for i in range(n-1):
    for j in range (n-i-1):
        if sum(l1[j])>sum(l1[j+1]):
            temp=l1[j]
            l1[j]=l1[j+1]
            l1[j+1]=temp
            
print(l1)



























