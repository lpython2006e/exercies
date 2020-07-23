n = input()
n = list(n)
so = []
chu = []
print(n)
for i in range(len(n)):
    n[i] = ord(n[i])
    if n[i] >= 97:
        chu.append(n[i])
    else:
        so.append(n[i])
n = chu + so
print(''.join(chr(i) for i in n))
