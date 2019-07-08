
n = input('Enter thr number: ')

try:
    print(10/int(n))
except ZeroDivisionError:
    print('Do not enter the Zero')
except ValueError:
    print('Enter the number')



