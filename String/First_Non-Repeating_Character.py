x = 'swiss'

def check(x):
    for i in range(len(x)):
        if x.count(x[i]) == 1:
            print(x[i])
            return

check(x)
