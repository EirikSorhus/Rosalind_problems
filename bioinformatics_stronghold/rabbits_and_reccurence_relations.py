
def fibonacci(n, k): # n is the month to count the number of rabits, k is the number of pairs of rabits per litter.
    fib_1 = 1
    fib_0 = 0
    if n < 0:
        print("incorrect input")
    elif n > 40:
        print("to large n input")
    elif k > 5:
        print("to large k input")
    if n == 0:
        return fib_0
    elif k == 0:
        return fib_1
    elif n == 1:
        return fib_1
    else:
        for i in range(2, n+1):
            fib = fib_1 + fib_0 * k # the rabits from previous generation cannot have children. So only the fib_0 is multiplied with k
            fib_0 = fib_1 # importent to change fib-0 to fib-1 first and then fib-1 to fib.
            fib_1 = fib
        return fib_1

print(fibonacci(5,3))


