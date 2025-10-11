import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


#  Step 1: Define the decorator
def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        run_time = end_time - start_time
        print(f"{function.__name__} run speed: {run_time}s")
    return wrapper_function


#  Step 2: Apply the decorator to your functions
@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


#  Step 3: Call the functions
fast_function()
slow_function()
