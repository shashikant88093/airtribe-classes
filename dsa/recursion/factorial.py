def factorial(n):
    if n ==1:
        return 1
    mul = factorial(n-1)
    mul = mul * n
    return mul


print(factorial(5))