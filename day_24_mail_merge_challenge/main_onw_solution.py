#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Here each name of invited_names and put in a list named "names"
with open("./Input/Names/invited_names.txt") as invited_names: #open the file to read it
    names = invited_names.readlines() # the .readlines() put each line of the file on a list "names"
print(f"names with \\n: {names}") #print to see how the list working

# new list to save each name as a each item with out the "\n" because that makes a line break on the letter
names_wout_slash_n = []  # new list empty
for i in range(len(names)): # this cylce is about ti iterate the number of the total items on the list "names"
    name_wosn = names[i].replace("\n", "") #this is a variable where we store each name wout "\n" every iterate
    names_wout_slash_n.append(name_wosn) #here we append each name wout "\n" in to the new empty list
print(f"names wout \\n: {names_wout_slash_n}") #print to see how the list goes

#this for loop itarate the number of total items(names) on the list  names_wout_slash_n
for i in range(len(names_wout_slash_n)):
    with open("./Input/Letters/starting_letter.txt") as starting_letter: #here open and read the startin letter (base letter)
        letter = starting_letter.read()
    new_letter = letter.replace("[name]", names_wout_slash_n[i]) #here we are replacing each name on each letter
    #new_letter save on each iteration a new letter with different name and then each letter
    #with each name is aout to create a new file bc doesn't exist already, and if is exist
    #is about to rewrite with the name used
    with open(f"./Output/ReadyToSend/{names_wout_slash_n[i]}", mode="w") as filetxt: #here we create or modify the file wth each name iterated
        letter = filetxt.write(new_letter) #here we write the letter
        #the letter is the new letter with the name replaced
        #and the file is the file created or modified with the name used
        #the mode "w" is to write the file, if the file exist it will be rewrite
        #if the file doesn't exist it will be created
        #the file is the file created or modified with the name used

    

    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp