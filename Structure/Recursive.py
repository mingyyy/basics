# Finding the nth Fibonacci number
# 1,1,2,3,5,8

# recursive solution with O(2**n)
def fib(n):
    if n <=1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


# memoization
def fib_m(n):
    return fib2(n, [0]*(n+1))


def fib2(n, l):
    if n <= 1:
        l[n] = 1
        return 1
    else:
        l[n] = fib2(n-1, l)+fib2(n-2, l)
        return l[n]

# bottom-up approach
def fib_up(n):
    if n <= 1:
        return 1
    else:
        m = 2
        a, b = 1, 1
        while n != m:
            c = a + b
            a, b = b, c
            m += 1
        return a+b

print(fib_up(5))