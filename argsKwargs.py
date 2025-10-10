#Args: You can use this if you are passing a variable number of arguments to a function.
#Kwargs: You can use this if you are passing a variable number of keyword arguments to a function.

def example_function(*args, **kwargs):
    print("Positional arguments (args):", args)
    print('Args type:', type(args)) #It will be a tuple
    print("Keyword arguments (kwargs):", kwargs)
    print('Kwargs type:', type(kwargs)) #It will be a dictionary

example_function(1, 2, 3, name="Alice", age=30)