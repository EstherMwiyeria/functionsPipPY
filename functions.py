# Write a Python function that takes two arguments (a and b) and returns their sum.
def addition(a,b):
    sum = a + b
    return sum
print(addition(2,5))
# Write a Python function that takes a string as input and returns the string reversed.
def word(name):
    return name[::-1]
print(word("beautiful"))


# Write a Python function that takes a list of integers as input and 
# returns the sum of all the integers in the list.
def sum_ints(ints):
    sum = 0
    for num in ints:
        sum += num
    return sum
print(sum_ints([1,2,3,4,5]))

# Write a Python function that takes a list of integers as input and returns 
# a new list with all the even numbers removed.
def list_of_ints(ints):
    empty = []
    for i in ints:
        if i % 2 != 0:
            empty.append(i)
    return empty
print(list_of_ints([1,2,3,4,5,6,7,8,9]))
# Write a Python function that takes a list of integers as input and 
# returns the highest value in the list.
def highest_value(ints):
    num = max(ints)
    return num
print(highest_value([1,2,3,4,5,6,7,8,9]))

# Write a Python function that takes a list of strings as input and returns a new list with
#  all the strings capitalized.
def capitalize_strings(names):
    return [name.capitalize() for name in names]
    
print(capitalize_strings(["nina","noni","amani","imani"]))

