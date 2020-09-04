"""Write a program that read the CSV and print to console as a table (row and column should be aligned, border using – and |)"""
import csv

file = open('huong.csv')
reader = csv.reader(file)
list_reader = list(reader)
print(list_reader)

for row in list_reader:
    print(row)

outputFile = open('huong.csv', 'w', newline='')
writer = csv.writer(outputFile)
writer.writerow(['Minh','03/12/99','minh@yopmail.com'])
writer.writerow(['Minh','03/12/99','minh@yopmail.com']),['Minh','03/12/99','minh@yopmail.com'],['Minh','03/12/99','minh@yopmail.com'],['Minh','03/12/99','minh@yopmail.com']


csvWriter = csv.writer(outputFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerows(['Huong','03/12/99','minh@yopmail.com'])
print(csvWriter)

