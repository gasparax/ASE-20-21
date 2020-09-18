# calculator.py

def sum (m, n):
    result = m
    if (n < 0):
        for i in range (abs(n)):
            result = result - 1
    else:
        for i in range (n):
            result = result + 1

    return result


# Substract n from m until it gets to 0
def divide (m, n):
    if n == 0:
        raise ZeroDivisionError

    result = 0
    negative = m > 0 and n < 0 or m < 0 and n > 0
    n = abs (n)
    m = abs (m)

    while (m - n >= 0):
        m = m - n
        result = result + 1

    result = -result if negative else result

    return result