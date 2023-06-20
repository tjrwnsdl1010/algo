import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(1,T+1):
    N,M = map(int,input().split())
    numbers = list(map(int,input().split()))
    min_num = sum(numbers)
    max_num = 0
#  구간 합의 시작점을 찾는 i 
    for i in range(N-M+1):
        # 시작점을 기준으로 오른쪽 M개의 합
        total = 0
        for j in range(M):
            total += numbers[i+j]

        if total < min_num:
            min_num = total
        if total > max_num:
            max_num = total

    result = max_num - min_num
    
    print(f'{T} {result}')
        
