import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1,T+1):
    building_num = int(input())
    building_list = list(map(int,input().split()))

    total = 0
    # 모든 건물들을 기준으로 반복
    for i in range(building_num):
        now = building_list[i] # 계속 초기화됨
        if now == 0: # 내 위치가 0이 아니라면 비교시작
            continue
        else:
            idx = [-2,-1,1,2] # 델타 사용
            max_tall = 0
            for j in range(4): # 양옆의 2개의 건물 비교
                comp = building_list[i+idx[j]] 
                if max_tall < comp: # 제일 큰 높이를 찾아 나와 비교하기위함
                    max_tall = comp

            if now > max_tall:
                view = now - max_tall
                total += view

        print(total)
                
