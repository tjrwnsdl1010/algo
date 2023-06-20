import sys
sys.stdin = open('input.txt')
from pprint import pprint
T = int(input())
for tc in range(1,T+1):
    N,K = map(int, input().split())

    arr = list(range(1,13))
    count = 0
    for i in range(1<<len(arr)):
        result = []
        for j in range(len(arr)):
            if i & (1<<j):
                result.append(arr[j])
        print(result)

        if len(result) == N and sum(result) == K:
            count += 1
    print(f'#{tc} {count}')
