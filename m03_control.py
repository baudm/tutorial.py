#!/usr/bin/env python3

# Conditionals
if True:
    print('1. True')

if not False and True:
    print('2. Still True')

if not not True or False:
    print('3. Double negative')


# Loops

# Ifini...
while True:
    print('Not an infinite loop.')
    # nope.
    break

# Create a list of numbers from [0, 5)
numbers = list(range(5))
# While the list is not empty...
while numbers:
    # Get the last item and print it
    print(numbers.pop())


print('\n')

# Iterate over range
for i in range(5):
    print(i)



# Define a set using literals
just_a_set = {1, 2, 3}

# Exception handling
try:
    first_element = just_a_set[0]
except TypeError as e:
    print('got error:', e)
else:
    print('got it:', first_element)
finally:
    print('always do this.')
