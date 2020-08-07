# SN,Name,Contribution
# 1,Linus Torvalds,Linux Kernel
# 2,Tim Berners-Lee,World Wide Web
# 3,Guido van Rossum,Python Programming

import csv
row_list = [
    ["ID", "Name", "Email"],
    ["A878", "Alfonso K. Hamby", "alfonsokhamby@rhyta.com"],
    ["F854", "Susanne Briard", "susannebriard@armyspy.com"],
    ["E833", "Katja Mauer", "kmauer@jadoop.com"]
]
csv.register_dialect('myDialect',
                     delimiter='|',
                     quoting=csv.QUOTE_ALL)
with open('office.csv', 'w', newline='') as file:
    writer = csv.writer(file, dialect='myDialect')
    writer.writerows(row_list)

# ID"|"Name"|"Email"
# "A878"|"Alfonso K. Hamby"|"alfonsokhamby@rhyta.com"
# "F854"|"Susanne Briard"|"susannebriard@armyspy.com"
# "E833"|"Katja Mauer"|"kmauer@jadoop.com"