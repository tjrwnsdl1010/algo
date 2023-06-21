import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = list(map(int, input().split()))

    string_map = []
    for str in range(N):
        string_map.append(input())


    result = []
    print(string_map)

    # 가로
    for row in range(N):
        # print(string_map[row])
        # 회문의 시작점만 반복
        for i in range(N-M+1):
            #회문인지 확인
            for j in range(M//2):
                # front : 앞글자
                f = string_map[row][i+j]
                # back 
                b = string_map[row][i+M-j-1]

                if f == b:
                    flag = True
                else:
                    flag = False
                    break
            # 회문을 찾음
            if flag:
                for k in range(M):
                    result += string_map[row][i+k]

    for col in range(N):
        for i  in range(N-M+1):
            for j in range(M):               
                f = string_map[i+j][col] 
                b = string_map[i+M-j-1][col]

                if f == b:
                    flag = True
                else:
                    flag = False
                    break
            # 회문을 찾음
            if flag:
                for k in range(M):
                    result += string_map[i+k][col]