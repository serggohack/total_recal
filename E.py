import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

prev = -1
max = 0
now_delay = 0

while True:
    now = int(input())
    if prev == 0 and now == 0:
       print(max) 
       break
    elif prev == now:
        now_delay += 1
    elif max < now_delay:
        max = now_delay
        now_delay = 1
    else:
        now_delay = 1
    prev = now