

f = open("test.csv", "a")
f.write("this is an append")

f = open("test.csv", "r")
content = f.read()
f1 = (f.readlines())

print (content)
