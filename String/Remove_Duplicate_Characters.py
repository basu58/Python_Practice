def remove_duplicate_char(x):
    li = list(x.upper())
    for i in range(len(li)-2):
        for j in range(i+1,len(li)-1):
            if li[i] == li[j]:
                li.remove(li[j])
    print(''.join(li))


str1 = 'Hello'
remove_duplicate_char(str1)

print(''.join(list(dict.fromkeys(str1))))
