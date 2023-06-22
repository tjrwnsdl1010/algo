import sys
sys.stdin = open('input.txt')

T = 10
for _ in range(1, T+1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        # 도착지를 찾는 코드
        if ladder[99][i] == 2:
            # x, y는 현재 나의 위치
            x = i
            y = 99

    # y == 0 이 되는 시점 => 제일 윗줄 도착
    while y > 0:
        # 현재 위치를 기준으로 좌우를 체크
        
        # 제일 오른쪽과 제일 왼쪽이 아니라면 => 좌우를 살펴보세요
        if x != 99 and x != 0:
            # 왼쪽을 보는경우
            if ladder[y][x-1] == 1:
                ladder[y][x] = 0
                x -= 1
                continue
            # 오른쪽을 보는경우
            if ladder[y][x+1]:
                ladder[y][x] = 0
                x += 1
                continue

        # 제일 오른쪽이라면 => 왼쪽만 살펴보세요
        elif x == 99:
            # 왼쪽을 보는경우
            if ladder[y][x-1] == 1:
                ladder[y][x] = 0
                x -= 1
                continue
        # 제일 왼쪽이라면 => 오른쪽만 살펴보세요
        elif x == 0:
            # 오른쪽을 보는경우
            if ladder[y][x+1]:
                ladder[y][x] = 0
                x += 1
                continue
            
        ladder[y][x] = 0
        y -= 1
    
    result = x
    print(result)