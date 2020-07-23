# Write a function that computes the running total of a list.
# def Cumulative(lists):
#     cu_list = []
#     length = len(lists)
#     cu_list = [sum(lists[0:x:1]) for x in range(0, length + 1)]
#     return cu_list[1:]
#
#
# lists = [10, 20, 30, 40, 50]
# print(Cumulative(lists))

a = range(20)

runningTotal = []
for n in range(len(a)):
    new = runningTotal[n - 1] + a[n] if n > 0 else a[n]
    runningTotal.append(new)

# This one is a syntax error
# runningTotal = [a[n] for n in range(len(a)) if n == 0 else runningTotal[n-1] + a[n]]

for i in zip(a, runningTotal):
    print("{0:>3}{1:>5}".format(*i))
