# 1. Printing the star pattern using for and while loop
# Using for loop
rows = 5
for i in range(1, rows + 1):
    print('*' * i)

# Using while loop
rows = 5
i = 1
while i <= rows:
    print('*' * i)
    i += 1

# 2. Printing the number pattern
# Using for loop
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

# Using while loop
rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print(j, end='')
        j += 1
    print()
    i += 1
