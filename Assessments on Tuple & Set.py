# Assessments on Tuple & Set

# 1. Write a Python program to create a tuple.
t = (5,8,9,1,6,4)
print(t)


# 2. Write a Python program to create a tuple with different data types
t1 = (1, "hello", 3.14, 12)
print(t1)


# 3. Write a Python program to create a tuple with numbers and print one item.
t2 = (20, 40, 60, 80, 30, 50, 70, 10)
print(t2[2])


# 4. Write a Python program to unpack a tuple in several variables.
t3 = (5, 2, 9)
x, y, x = t3
print(x, y, x)


# 5. Write a Python program to add an item in a tuple.
t4 = (9, 25, 13)
t5 = t4 + (4,)
print(t5)


# 6. Write a Python program to convert a tuple to a string.
t6 = ('P', 'A', 'V', 'A', 'N')
s = ''.join(t6)
print(s)



# 7. Write a Python program to get the 4th element and 4th element from last of a tuple.
t7 = (10, 20, 30, 40, 50, 60, 70, 80)
print(t7[3])
print(t7[-4])


# 8. Write a Python program to reverse a tuple.
t8 = (1, 3, 5, 7, 9, 11, 13, 15)
print(t8[::-1])


# 9. Write a Python program to find the repeated items of a tuple
t9 = (1, 2, 3, 2, 4, 5, 2)
print(t9.count(2))

# 10. Write a Python program to check whether an element exists within a tuple.
t10 = (12, 6, 3, 4, 5, 9, 15)
print(3 in t)


# 11. Write a Python program to convert a list to a tuple.
l = [11, 12, 13, 14, 15]
t11 = tuple(l)
print(t11)


# 12. Write a Python program to remove an item from a tuple.
t12 = (5, 6, 7, 8, 9, 10, 11)
t12 = tuple(x for x in t if x != 3)
print("Tuple after removing 3:", t12)


# 13. Write a Python program to slice a tuple.
t13 = (7, 20, 34, 14, 50, 6, 27)
print(t13[2:5])


# 14. Write a Python program to find the index of an item of a tuple.
# 15. Write a Python program to find the length of a tuple.
t14 = (10, 20, 30, 40, 50)

print(t14.index(30))
print(len(t14))



# 16. Write a Python program to sort list of tuple based on sum
# Input: [(4, 5), (2, 3), (6, 7), (2, 8)]
# Output: [(2, 3), (4, 5), (2, 8), (6, 7)]"
l1= [(4,5), (2,3), (6,7), (2,8)]
n = len(l1)

for i in range(n - 1):
    for j in range(n - i - 1):
        if sum(l1[j]) > sum(l1[j + 1]):  # Compare sums
            l1[j], l1[j + 1] = l1[j + 1], l1[j]  # Swap

print(l1)






















