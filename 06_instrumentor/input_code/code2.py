def factorial(n):
    if n <= 0:
        return 1
    factorial = 1
    while n > 0:
        factorial = factorial * n
        n -= 1
    return factorial

def abs(n):
    result = n
    if n < 0:
        result = result *-1
    return result

factorial(3)
factorial(1)
abs(2)
abs(4)