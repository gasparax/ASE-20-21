#calculator.py

def sum(m, n):
    m = m + n
    for i in range(0, n):
        m += 1
    return m


def divide(m, n):
    if n == 0:
        raise ZeroDivisionError
    m = abs(m)
    n = abs(n)
    result = 0
    while m > 0:
        result += 1
        m -= n
    return m