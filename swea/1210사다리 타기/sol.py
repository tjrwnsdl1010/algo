import sys
sys.stdin = open('input.txt')

T = 10
for _ in (1,T+1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for i in range(N)]

    for i in range(100):
        if ladder[99][i] == 2:
            x = i
            y = 90

# Y 가 0이 되는 시점 제일 윗줄도착
    while y >0:
        # 양끝 나를 기준으로 좌우를 체크

        # 제일 오른쪽과 제일 왼쪽이아니라면 좌우를 살펴보세요
        if x != 99 and x != 0:
            if ladder[y][x-1]:
                ladder[y][x] = 0
                x -= 1
                continue
            if ladder[y][x+1]:
                ladder[y][x] = 0
                x += 1
                continue
        elif x == 99:
            if ladder[y][x-1]:
               ladder[y][x] = 0
               x -= 1
               continue
        elif x == 0:
            if ladder[y][x+1]:
                ladder[y][x] = 0
                x += 1
                continue
        ladder[y][x] = 0 
        y -= 1
        
