def fib_master(value):
    cache={}
    def fib(n):
        if n in cache:
            return cache[n]
        elif n<2:
            return n
        else:
            cache[n] = fib(n-1)+fib(n-2)
            return cache[n]
    return fib(value)

print(fib_master(11))