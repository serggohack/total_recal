import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

for i in range(5):
    a, b, c = [int(i) for i in input().split()]
    if a <= 23 and b <= 59 and c <= 59:
        print("YES")
    else:
        print("NO")