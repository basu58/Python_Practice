def fibonacci(x):
    a = 0
    b = 1

    for i in range(x):
        a, b = b, a + b

    return a

print(fibonacci(10))