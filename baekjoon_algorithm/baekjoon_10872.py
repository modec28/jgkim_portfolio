def factorial(i):
    if i > 0 :
        return i*factorial(i-1)
    return 1

print(factorial(int(input())))
