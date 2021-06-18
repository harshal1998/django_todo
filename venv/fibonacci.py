n = int(input("enter how many no of fibonacci series u want:"))


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


for i in range(n + 1):
    print(fib(i))
