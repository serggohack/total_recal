import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

a = int(input())

if a <= 0:
    print("NO")
    print(2)
elif a % 2 == 0:
    print("YES")
    print(a + 2)
else:
    print("NO")
    print(a + 1)