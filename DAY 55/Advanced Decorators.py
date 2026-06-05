# https://flask.palletsprojects.com/en/stable/quickstart/#routing
# https://flask.palletsprojects.com/en/stable/quickstart/#variable-rules
# https://youtu.be/BnBJVh1DBGw?si=BucIPyxoOjj-xd59
# https://youtu.be/A9j2V2SPq3g?si=-NmULeo-nPm1Wvc8
"""
Create a logging_decorator() which is going to print the name of the function that was called, the arguments it was given and finally the returned output:
You called a_function(1,2,3)
It returned: 6
The value 6 is the return value of the function.
Don't change the body of a_function.
IMPORTANT: You only need to use *args, you can ignore **kwargs in this exercise.
"""
def logging_decorator(func):
    def wrapper(*args):
        print(f"You called the {func.__name__}{args}")    #before decorator
        results = func(*args) #execute of decorator
        print(results) #after decorator
        return results
    return wrapper

@logging_decorator
def a_function(*args):
    return sum(args)

a_function(1, 2, 3)


