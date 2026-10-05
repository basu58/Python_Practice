s = 'Hello'
print(''.join(reversed(s)))

def reverse_string(s):
    str1 = ''
    for i in range(len(s) - 1, -1, -1):
        str1 = str1 + s[i]
    print(str1)


reverse_string(s)