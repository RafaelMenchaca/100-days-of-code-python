import csv

with open('day_62_flask_wtforms_bootstrap\day_62\cafe-data.csv', newline='', encoding='utf-8') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    list_of_rows = []
    for row in csv_data:
        list_of_rows.append(row)
    cafes = list_of_rows

# print(cafes)
# print(cafes)

# print(cafes[0])

for cafe in cafes:
    print(cafes[0][1])
    # print(cafe[0])  # Print the name of each cafe
