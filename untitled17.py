# Assessments on List

# 1. WAP to remove to find duplicates elements in list,
def remove_duplicates(lst):
   return list(set(lst))
    
lst=[1,2,2,3,4,4,5]
print(remove_duplicates(lst))

# 2. WAP to sort the given list.
def sort_list(lst):
    return sorted(lst)

l=[5,9,3,6,4,8,1,2]
print(sort_list(l))

# 3. WAP to create a list such that new list contains alternate even and odd from given list
# 	l1=[45,77,23,45,66,88,22,12]
#       l2=[45,66,77,88,23,22,45,12]
l1=[45,77,23,45,66,88,22,12]
l2=[45,66,77,88,23,22,45,12]
def alternative_even_odd(l1,l2):
    even=[]
    odd=[]
    return result

    for num in l1:
        if num%2==0:
            even.append(num)
        else:
            odd.append(num)  
            
    for num in l2:
        if num%2==0:
            even.append(num)
        else:
            odd.append(num)
result=[]

print(alternative_even_odd(l1, l2))        
            
            
4. Write a Python program to get the largest number from a list.
def find_largest(lst):
    return max(lst)

l1=[10,50,23,60,98,10]
print(find_largest(l1))

# 5. Write a Python program to count the number of strings where the string length is 2 
def count_strings(lst):
    count=0
    for string in lst:
        if len(string)>=2:
          count+=1
    return count   

l2=["Hi","Ok","No","Yes","of"]
print(count_strings(l2))

# 7. Write a Python program to find the list of words that are longer than given words
def longer_words(lst, length):
    return 
# 8. Write a Python function that takes two lists and returns True if they have at least one common member.
def common_element(l5,l6):
    return any[ele in l5 for ele in l6]

l5=[1,2,8,9,5,6]
l6=[1,3,5,9,2,8,4]
print(common_element(l5,l6))

# 9. Write a Python program to print a specified list after removing the 0th, 4th and 5th
# elements. Go to the editor
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
def remove_elements(lst):
    return lst[]
        for i in range(len(lst)):
            if i!=0 and i!=4 and i!=5:
                new_list.append(lst[i])
        return new_list()

lst=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] 
print(remove_elements(lst))              
