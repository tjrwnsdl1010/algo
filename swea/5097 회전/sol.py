import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().spilt())

    numbers = list(map(int,input().spilt()))

    for _ in range(M):
        # 맨 앞에 요소 빼기
        deq = numbers.pop(0)
        # 맨 뒤에 추가하기
        numbers.append(deq)
    