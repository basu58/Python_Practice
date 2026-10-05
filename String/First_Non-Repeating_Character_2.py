x = 'swiss'

def check(x):
    res = {}

    for i in range(len(x)):
        if x[i] in res:
            res[x[i]] = res[x[i]] + 1
        else:
            res[x[i]] = 1

    for char in x:
        if res[char] == 1:
            print(char)
            return


check(x)
