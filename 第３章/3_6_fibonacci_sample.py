# This function returns a list of n Fibonacci numbers

def fibonacci(n):
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-2] + fib_list[-1])
    return fib_list


print(fibonacci(10))
