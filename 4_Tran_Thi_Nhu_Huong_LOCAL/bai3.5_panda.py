"""Write a program that read the CSV and print to console as a table (row and column should be aligned, border using – and |)"""
import pandas

file = pandas.read_csv("huong.csv")
print(file)
