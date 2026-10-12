def longest_word(x):
    li = x.split(' ')
    dic1 = {}
    for i in li:
        if i not in dic1:
            dic1[i] = len(i)
    dic1 = dict(sorted(dic1.items(), key = lambda item: item[1], reverse=True))
    print(list(dic1.keys())[0])

x = "Python is extremely powerful"
longest_word(x)