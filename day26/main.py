# numbers = [1, 1, 2, 3, 4, 5, 8, 13, 21, 34, 55]
#
# # Your code below
# squared_numbers = [num * num for num in numbers]
# # Your code above
#
# print(squared_numbers)


###

list_of_strings = input().split(",")
# Do not change code above.

# TODO: Use list comprehension to convert strings to integer
list_of_integer = [int(item) for item in list_of_strings]
# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
result = [item for item in list_of_integer if item%2 == 0]
# Write your code above:
print(result)