file = open("my_file.txt") # open the file
contents = file.read() # read the file
print(contents)
file.close() # close the file after taking all the needed resources

''' instead of writing file.close()  '''

with open("my_file.txt") as file:  # in this way the file is closed automatically
    content = file.read()
    print(content)

''' what if i want to write inside that file '''

with open("my_file.txt", mode ="a") as file: # to write inside the file we should change the mode into "a" or "w"
    # mode = "a" if you want to add a text without deleting any previous texts
    # mode = "w" if you want to add a text and delete all the previous texts
    file.write("\nNew text.")

with open(r"C:\Users\emand\OneDrive\Desktop\new_file.txt", mode = "a") as file: # If the file does not exist, it will be created automatically.
    file.write("\nNew text.")

