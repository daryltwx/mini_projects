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


###


f = open("file1.txt", "r")
file1 = f.readlines()
ls = [int(num.rstrip()) for num in file1]

f2 = open("file2.txt", "r")
file2 = f2.readlines()
ls2 = [int(num.rstrip()) for num in file2]


list = ls + ls2

result = [x for x in ls if x in ls2]
# Not needed to add everything in a list, just compare each list.
#result = [x for x in list if list.count(x) > 1]

# Write your code above 👆
print(result)



###


# Using list comprehension in US states game

if answer_state == "Exit":
    missing_states = []
    for state in all_states:
        if state not in guessed_states:
            missing_states.append(state)
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")
    break

if answer_state == "Exit":
    missing_states = [state for state in all_states if state not in guessed_states]
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")
    break



###

# Dictionary Comprehension

