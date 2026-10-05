x = 'Hello Welcome To Python Learnings'

res = {}

for i in range(len(x)):
    if x[i] in res:
        res[x[i]] = res[x[i]] + 1
    else:
        res[x[i]] = 1

print(res)
