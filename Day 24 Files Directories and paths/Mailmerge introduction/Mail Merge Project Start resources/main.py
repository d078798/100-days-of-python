#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


import os

with open("Day 24 Files Directories and paths\\Mailmerge introduction\\Mail Merge Project Start resources\\Input\\Letters\\starting_letter.txt", "r") as f:
    # Day 24 Files Directories and paths\\Mailmerge introduction\\Mail Merge Project Start resources\\Input\\Letters\\starting_letter.txt
    letter_template = f.read()
    
with open("Day 24 Files Directories and paths\\Mailmerge introduction\\Mail Merge Project Start resources\\Input\\Names\\invited_names.txt" , "r") as f:
    names_contents = f.read()
names_list = names_contents.split("\n")

for name in names_list:
    print(name)
    
    new_letter = letter_template.replace("[name]", name)
    with open(f"Day 24 Files Directories and paths\\Mailmerge introduction\\Mail Merge Project Start resources\\Output\\ReadyToSend\\{name}_letter.txt", "w") as f:
        f.write(new_letter)
        print("\tSaved")
    
    