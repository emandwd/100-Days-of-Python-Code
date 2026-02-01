PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./INput/Letters/starting_letter.docx") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/Letter_for_{stripped_name}.docx", mode ="w") as completed_letter :
            completed_letter.write(new_letter)

# read() → Reads the entire file as a single string
# readlines() → Reads the file line by line into a list of strings
# strip() → Removes leading and trailing whitespace (spaces, \n, \t) from a string