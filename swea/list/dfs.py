import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())
for tc in (1,T+1):
    V,E = list(map(int,input().split()))

    nodes = [[0]*(V+1) for _ in range(V+1)]

    for line in range(E):
        start,end = list(map(int,input().split()))

        nodes[start][end] = 1
    # S는 확일 해야하는 출발 노드
    # G는 연결이 되어있음을 확인하는 도착노드
    S,G = list(map(int,input().split()))

    #dfs를 하기위해 과거를 기록하는 stack
    stack = []

    # 내가 방문했던 기록을 남기는 체크리스트
    check_list = [False]*(V+1)


    # v는 현재 위치
    v = S
    check_list[v] = True
    stack.append(v)
    result = 0
    while len(stack): 
        # 현재 나의 노드와 연결된 노드를 탐색
        for w in range(V+1):
            if nodes[v][w] == 1:
                # 아직 방문을 안했다면
                if not check_list[w]:
                    # 연결된 노드(v)를 방문처리
                    check_list[w] = True
                    # 나의 노드(v)를 stack에 push
                    stack.append(v)
                    # 현재 위치를 이동
                    v = w
                    #경로에 목적지가 있으면 저장
                    if w == G:
                        result =1

                    break
        else : 
            v = stack.pop()

    print(f'#{tc} {result}')