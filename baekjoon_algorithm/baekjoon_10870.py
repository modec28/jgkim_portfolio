def Fibonacci(i):
    if i > 0 :
        a = sum(f)
        f[0] = f[1]
        f[1] = a
        return Fibonacci(i-1)
    return f[0]
f = [0,1]
print(Fibonacci(int(input())))
