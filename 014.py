import sys

print(sys.argv)

x = sys.argv[1]
'''
x = input('Enter anything: ')
'''
try:
    int(x)
    print(x,' is number')
except:
    print('This is string.')


