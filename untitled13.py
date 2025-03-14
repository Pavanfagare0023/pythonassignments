# 1. Python program to remove given character from String.
s1="A good traveler has no fixed plans"
s1=s1.replace("no", "")
print(s1)

# # 2. Python Program to count occurrence of a given characters in string.
print(s1.find("traveler"))

# 3. Python program to check a String is palindrome or not.
s2=s1[::-1]

if s1==s2:
    print('string is pallimdrome')
else:
    print('string is not pallimdrome') 

# 4. Python program to check given character is vowel or consonant.
chr=input('Enter a Character: ')
if chr in'aeiou':
    print('{chr} is a vowel')
else:
    print('{chr} is a consonant')

# 5. Python program to check given character is digit or not.
char = input("Enter a character: ")
if char.isdigit():
   print(f"'{char}' is a digit")
else:
   print(f"'{char}' is not a digit")

# 6. Python program to check given character is digit or not using isdigit() method.
s3="The number 3264 emplyee leave the company year ago"
print(s3.isdigit())

# 7. Python program to replace the string space with a given character.
text = "Develop success from failures"
char = "-"
print(text.replace(text, char))


# 8. Python program to replace the string space with a given character using replace() method.
str="Larsen & Turbo"
char = "_"
str = str.replace(" ", char)
print(str)

# 9. Python program to convert  char to uppercase of string.
chr= "uneducated genius is almost proverb"
print(chr.upper())

# 10. Python program to convert lowercase vowel to uppercase in string.


# 11. Python program to delete vowels in a given string.
str= "The rain fell steadily"
for c in str:
    if c not in "aeiouAEIOU":
       str += c 
    print(str)
    
# 12. Python program to count Occurrence Of Vowels & Consonants in a String.


# 13. Python program to count alphabets, digits and special characters.
s5="There are 500 cars @ backyards"

alphabets=0
digits=0
special_chr=0

for c in s5:
    if c.isalpha():
        alphabets += 1
    elif c.isdigit():
        digits += 1
    else:        
        special_chr += 1
        
print("alphabets:", alphabets)
print("digits:", digits)
print("special_chr:", special_chr)
        
        
# 14. Python program to separate characters in a given string.
s6="World is so fast"

for b in s6:
    print(b)
    
    
# 15. WAP to replace every character by its next subsequent character.

