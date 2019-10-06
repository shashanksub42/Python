#Naive Recursion
def fib_recursion(n):
    if n <= 2:
        return 1
    else:
        f = fib_recursion(n-1) + fib_recursion(n-2)

    return f

#Memoization
memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    else:
        f = fib_memo(n-1) + fib_memo(n-2)
    memo[n] = f
    return f

#Bottom up
def fib_bottom_up(n):
    fib = {}
    for k in range(1, n+1):
        if k <= 2:
            fib[k] = 1
        else:
            fib[k] = fib[k-1] + fib[k-2]
            del fib[k-2]
    return fib[n]


for i in range(1, 20):
    print(fib_bottom_up(i))
