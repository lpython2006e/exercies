"""Write a program that read the CSV and print to console as a table (row and column should be aligned, border using – and |)"""
import csv
from prettytable import from_csv

file = "huong.csv"
with open("huong.csv", "r") as fp:
    x = from_csv(fp)

print(x)