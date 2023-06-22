import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in (1,T+1):
    N,M = map(int,input().split())
    bug_board = [list(map(int, input().split())) for i in range(N)]
    
    result = 0
    for row in range(N-M+1): # 4번 배열탐색 out of range 방지, 기준점
        for col in range(N-M+1): 
            total = 0
            for i in range(M):  # 파리채 위치 탐색
                for j in range(M):  
                    total += bug_board[row+i][col+j]
            if result < total:
                result = total

                
                    
        

