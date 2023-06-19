import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):    
    K,N,M = map(int, input().split())
    station = list(map(int, input().split()))

now = 0
charge = 0
move = now+K
count = 0

while move < N:
    for i in station:
        if now < i <= move:
            charge = i
        


