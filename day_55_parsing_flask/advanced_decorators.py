#  Step 1: Create the decorator
def logging_decorator(function):
    def wrapper(*args):
        # Print function name and arguments
        print(f"You called {function.__name__}{args}")

        # Call the original function and get the result
        result = function(*args)

        # Print return value
        print(f"It returned: {result}")

        return result  # Don’t forget to return it!

    return wrapper


#  Step 2: Apply the decorator
@logging_decorator
def a_function(*args):
    return sum(args)


#  Step 3: Call the function
a_function(1, 2, 3)
