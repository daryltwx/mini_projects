#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER_NAME = "[name]"


with open("/Users/Pandaphy/github/mini_projects/day24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_text:
    letter = letter_text.read()
    print(letter)


with open("/Users/Pandaphy/github/mini_projects/day24/Mail Merge Project Start/Input/Names/invited_names.txt") as name_list:
    names = name_list.read().split("\n")
    print(names)


for name in names:
    with open(f"/Users/Pandaphy/github/mini_projects/day24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", "w") as list:
        new_letter = letter.replace(PLACEHOLDER_NAME, name)
        list.write(new_letter)