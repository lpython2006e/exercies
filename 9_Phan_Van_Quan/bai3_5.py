#Write a program that read the CSV and print to console as a table
# (row and column should be aligned, border using – and |)


from prettytable import from_csv

with open("classmate.csv", "r") as fp:
    x = from_csv(fp)

print(x)

# import csv
# with open('classmate.csv', 'r') as file:
#     reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
#     for row in reader:
#         print(row)