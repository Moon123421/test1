x = int(input('number'))
def fac(n):
    if n == 0:
        return 1
    return n * fac(n-1)

print(fac(x))



