
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 6,4,5,6,31,234,2))
print()

def calculate(**kwargs):
    print(kwargs)

calculate(add=3, multiply=5)