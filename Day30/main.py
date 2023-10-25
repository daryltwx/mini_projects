# try:
#     file = open("a_file.txt")
#     a_dict = {"key":"no"}
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"{error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#    raise KeyError("No no no no noooooo! ")
#

height = float(input("Height in Meters: "))
weight = int(input("Weight in kg: "))

if height > 3 or height < 0 or weight > 400 or weight < 20:
    raise ValueError("Human Height should not be over 3 meters. ")

bmi = weight / height ** 2
print(bmi)