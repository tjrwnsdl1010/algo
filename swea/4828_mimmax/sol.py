import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    numbers.sort()
    for i in range(len(numbers)):
        result = numbers[-1]-numbers[0]
    print(f'#{tc} {result}')