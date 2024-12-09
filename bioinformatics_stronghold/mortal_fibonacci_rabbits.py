# Mortal fibanachi

def fibonacci(n, m): # n is the month to count the number of rabits, m is the number of moths the rabbits live.
    fib_1 = 1
    fib_0 = 0
    if n < 0:
        print("incorrect input")
    elif n > 100:
        print("to large n input")
    elif m > 20:
        print("to large m input")
    elif m == 0:
        print("to small m input")
    elif m == 1:
        return fib_0
    elif m == 2:
        return fib_1
    elif n == 0:
        return fib_0
    elif n == 1:
        return fib_1
    else:
        for i in range(2, n+1):
            fib = fib_1 + fib_0 * m # the rabits from previous generation cannot have children. So only the fib_0 is multiplied with k
            fib_0 = fib_1 # importent to change fib-0 to fib-1 first and then fib-1 to fib.
            fib_1 = fib
        return fib_1

print(fibonacci(5,3))

1 1 2 3 5 8 13 21   uendelig
1 1 2 2 3 4 5       3
1 1 1 1 1 1 1       2
1 1 2 3 
