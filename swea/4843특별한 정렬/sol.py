import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(len(numbers)-1,0,-1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    result = []

    for i in range(5):
        result.append(numbers[-i-1])
        result.append(numbers[i])

    result = ' '.join(map(str,result))
    print(f'#{tc} {result}')

