
def facto(a):
    i = 0
    val = 1
    while i < int(a):
        i += 1
        val *= i
    return(val)


x = int(input('Enter the number: '))
print(facto(x))





