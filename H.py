import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

input()

a = [int(i) for i in input().split()]

odd = []
even = []

for i in a:
    if i % 2 == 0:
        odd.append(i)
    else:
        even.append(i)

for i in odd:
    print(i, end=" ")

for i in even:
    print(i, end=" ")