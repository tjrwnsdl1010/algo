import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    K,N,M = map(int, input().split())

    bus_stop = list(map(int,input().split()))
    cnt = 0
    now = 0

    # 충전할 필요 없이 바로 도착하는 경우 
    if K >= M:
        cnt = 0
    # 충전하면서 지나가야할떄
    else : 
        # 버스가 종점에 도착하지 않았다면 계속 반복
        while now < N:
            # 현재 위치에서 최대로 갈 수 있는 정류장을 찾는다.
            # 최대로 갈수 있는 범위(now+K)부터 현재위치(now)까지 반복
            for i in range(now+K, now, -1):
                # 1. 최대 범위가 종점을 넘는 경우
                if i >= N:
                         now = N
                         break
                # 2. 최대 범위가 종저을 아직 못넘은 경우
                if i in bus_stop:
                     # 가장 뒤에 있는 충전소로 이동
                     now = i
                     #충전을 하고 이동했으니 카운트 증가
                     cnt += 1
                     break
                    # 현재 위치(now)에서 최대 거리를 찾았는데 충전소가 없으면 도착 불가능
            else:
                 cnt = 0
                 now = N

    print(f'{T} {cnt}')

    

