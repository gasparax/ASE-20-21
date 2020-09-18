#calculator.py

def sum(m, n):
    m = m + n
    for i in range(0, n):
        m += 1
    return m


def divide(m, n):
    while m > 0:
        m -= n
    return m