import math
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

(a, b, c) = [int(s) for s in input().split()]
(h, l) = [int(s) for s in input().split()]

s=2*a*c+2*b*c+a*b
rulon=h*l/1000000
s=s*0.85
s=s*1.1
s=s/rulon
s=math.ceil(s)
print(s)

 