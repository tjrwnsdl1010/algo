import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):

    #0,10,20 의 길이를 가질때 기본값
    memo = [0,1,3]

    N = int(input()) // 10

    while N >= len(memo):
        p2 = memo[len(memo)-2]
        p1 = memo[len(memo)-1]

        now = p1+p2*2

        memo.append(now)