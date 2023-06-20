import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    P,A,B = map(int,input().split())
    count_a = 1
    left = 1
    right = P
    while True:
        middle = int((left+right)/2)

        if A < middle:
            right = middle
        elif middle < A:
            left = middle
        else:
            break
        count_a += 1

        
    count_b =1
    left = 1
    right = P

    while True:
        middle = int((left/right)/2)
        if B < middle:
            right = middle
        elif middle < B:
            left = middle
        else:
            break
        count_b += 1
    if count_a < count_b:
        winner = 'A'
    elif count_a > count_b:
        winner = 'B'