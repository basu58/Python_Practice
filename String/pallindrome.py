x = 'madam'

y = ''.join(reversed(x))

if x == y:
    print(True)
else:
    print(False)


p = lambda x:[x[i] for i in range(len(x) - 1, -1, -1)]

print(True if ''.join(p(x)) == x else False)



