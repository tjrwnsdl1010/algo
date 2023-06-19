import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int, input()))

    cnt_list = [0 for i in range(10)]
    
    for number in numbers:
        cnt_list[number] +=1

    max_cnt = 0

    for idx, count in enumerate(cnt_list):
        if max_cnt <= count:
            result = idx
            max_cnt = count

    print(f'#{tc} {result} {max_cnt}')