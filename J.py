import math
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

ans = 0

a = input().split()

for i in a:
    if len(i) % 2 == 1:
        if i[:math.ceil(len(i) / 2)] == i[math.ceil(len(i) / 2) - 1:][::-1]:
            ans += 1
    else:
        if i[:len(i) // 2] == i[len(i) // 2:][::-1]:
            ans += 1

print(ans)