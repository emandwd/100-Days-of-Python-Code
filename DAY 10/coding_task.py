def format_name(f_name, l_name) :
  if f_name == "" or l_name == "" :
    return " You did not provide valid inputs "
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"
  print(" hi, how are you ")
  """ nothing will be printed here because return tells the 
  function to stop and it is the end of the function the program will not read anything after it """

format_string = format_name(input("What is your first name? " ) , input("What is your last name?"))
print(format_string)

def function_1(text) :
    return text + text
def function_2(text) :
    return text.title()
output = function_1("hello")
output2 = function_2(output)
print(output2)


""" those types of comments is called Docstrings """