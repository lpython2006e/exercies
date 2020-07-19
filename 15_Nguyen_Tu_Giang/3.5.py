# Write a program that read the CSV and print to console as a table (row and column should be aligned, border using – and |)
import csv

print('What is the path of file:')
url = input()
# initializing the titles and rows list
fields = []
rows = []
# reading csv file
try:
    f = open(url, 'r')
    # creating a csv reader object
    csv_reader = csv.reader(f)
    # extracting field names through first row
    fields = next(csv_reader)
    # extracting each data row one by one
    for row in csv_reader:
        rows.append(row)
    # get total number of rows
    print('Total list classmate:', csv_reader.line_num)
    # printing the field names
    print('Name of fields:', fields)
    print('The list of classmate:')
    for row in rows:
        # parsing each column of a row
        for col in row:
            print("%s |" % col),
            print('------')
        # print('\n')
        # print('---')
except FileNotFoundError:
    print('File not accessible.')
