# import sys
# sys.stdin = open('input.txt')
# from pprint import pprint
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())

#     board = [[0 for _ in range(10)] for _ in range(10)]
#     pprint(board)
#     for i in range(N):
#         color_data = list(map(int, input().split())) 
#         left_top_x = color_data[0]
#         left_top_y = color_data[1]
#         rigt_bottom_x = color_data[2]
#         right_bottom_y = color_data[3]

#         color = color_data[4]

#         for x in range(left_top_x,rigt_bottom_x+1):
#             for y in range(left_top_y,right_bottom_y+1):
#                 board[x][y] += color
#     count = 0
#     for x in range(10):
#         for y in range(10):
#             if board[x][y] == 3:
#                 count += 1


# 부분집합
numbers = [2,5,1,4]

n = len(numbers)

# 1을 두번씩 곱해간다 => 2^4
for i in range(1<<n):
    # print(bin(i), end= ',')
    for j in range(n):
        if i & (1<<j):
            print(numbers[j],end = ',')
            
            
    