import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

a = input()

minu = False

if a[0] == '-':
    minu = True
    a = a[1:]

a = a[::-1]

if minu:
    a = '-' + a

print(int(a))
