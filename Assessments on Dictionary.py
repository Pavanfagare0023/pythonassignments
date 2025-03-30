# Assessments on Dictionary

# 1. Write a Python program to combine two dictionary adding values for
# common keys. Go to the editor
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
combined_dict = d1 + d2
print("Combined Dictionary:", combined_dict)


# 2. Write a Python program to print all unique values in a dictionary.
# Original List: [{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII':
# 'S005'}, {'V': 'S009'},
# {'VIII': 'S007'}]
# Unique Values: {'S009', 'S002', 'S007', 'S005', 'S001'}
original_list = [{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, 
                 {'VII': 'S005'}, {'V': 'S009'}, {'VIII': 'S007'}]
unique_values = {val for dic in original_list for val in dic.values()}
print("Unique Values:", unique_values)


# 3. Write a Python program to create a dictionary from a string.
# Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
sample_string = 'w3resource'
letter_count = {char: sample_string.count(char) for char in set(sample_string)}
print("Letter Count Dictionary:", letter_count)


# 4. Merge following two Python dictionaries into one.
# Get the key corresponding to the minimum value from the following
# dictionary
# sampleDict = { 'Physics': 82, 'Math': 65, 'history': 75}
# Expected output: Math
sampleDict = {'Physics': 82, 'Math': 65, 'History': 75}
min_key = min(sampleDict, key=sampleDict.get)
print("Key with minimum value:", min_key)



# 5. Combine two dictionary adding values for common keys
# Input: dict1 = {'a': 12, 'for': 25, 'c': 9}
# dict2 = {'python': 100, 'java': 200, 'for': 300}
# Output: {'for': 325, 'python': 100, 'java': 200}
dict1 = {'a': 12, 'for': 25, 'c': 9}
dict2 = {'python': 100, 'java': 200, 'for': 300}
combined_dict2 = dict1 + dict2
print("Combined Dictionary 2:", combined_dict2)


# 6. dict1={101:{“Apple” :10, “Mango” :5 },
# 102 :{“Apple” :15, “Mango” :8, “Cherry” :5 },
# 103: {“Apple” :10} }
# Output
# Dict2= {“ Apple” :35, “Mango” :13, “Cherry” :5 }
dict1 = {101: {"Apple": 10, "Mango": 5},
         102: {"Apple": 15, "Mango": 8, "Cherry": 5},
         103: {"Apple": 10}}

dict2 = ()
for sub_dict in dict1.values():
    dict2.update(sub_dict)
print("Summed Dictionary:", dict(dict2))