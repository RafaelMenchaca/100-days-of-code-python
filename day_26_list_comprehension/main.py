# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(n) for n in list_of_strings]
# print(numbers)
# result = [n for n in numbers if n % 2 == 0]
# print(result)


with open("./file1.txt") as file:
    file1 = file.readlines()
stripped_name_file1 = [int(n.strip()) for n in file1]

with open("./file2.txt") as file:
    file2 = file.readlines()
stripped_name_file2 = [int(n.strip()) for n in file2]

result = [n for n in stripped_name_file1 if n in stripped_name_file2]
print(result)