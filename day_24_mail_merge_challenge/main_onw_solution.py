#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


# Step 1: Read names from the invited_names.txt file
with open("./Input/Names/invited_names.txt") as invited_names_file:
    names = invited_names_file.readlines()  # .readlines() reads each line into a list item

print(f"Names with '\\n': {names}")  # Debug print: shows the raw names list including newline characters

# Step 2: Clean the names (remove the '\n') and save them into a new list
names_without_newline = []  # Empty list to store clean names

for i in range(len(names)):  
    name_clean = names[i].replace("\n", "")  # Remove newline character from each name
    names_without_newline.append(name_clean)  # Add the clean name to the new list

print(f"Names without '\\n': {names_without_newline}")  # Debug print: shows clean names list

# Step 3: Create and save a personalized letter for each name
for i in range(len(names_without_newline)):
    # Open and read the starting letter template
    with open("./Input/Letters/starting_letter.txt") as starting_letter_file:
        letter_template = starting_letter_file.read()

    # Replace the placeholder [name] with the actual name
    personalized_letter = letter_template.replace("[name]", names_without_newline[i])

    # Save the personalized letter into a new file named after the invitee
    with open(f"./Output/ReadyToSend/{names_without_newline[i]}", mode="w") as output_file:
        output_file.write(personalized_letter)


    

    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp