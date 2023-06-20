arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12],
]
row_count =len(arr)
column_count = len(arr[0])

# 가로를 기준으로 완전탐색
for row in range(row_count):
    for column in range(column_count):
        print(row, column,arr[row][column])

#세로를 기준으로 완전탐색
for column in range(column_count):
    for row in range(row_count):
        print(row,column,arr[row][column])

#지그재그 완전탐색(별로안씀)

for row in range(row_count):
    for column in range(column_count):
        print(arr[row][column+(column_count-1-2*column)*(row%2)])
        # print(arr[row][(column_count - column - 1)*(row%2)])

# 델타 이용
arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12],
]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

for x in range(len(arr)):
    for y in range(len(arr[0])):
        print(f'현쟈 위치는 {arr[x][y]}')

        for i in range(4):
            temp_x = x+dx[i]
            temp_y = y+dy[i]

            if 0 <= temp_x < len(arr) and 0 <= temp_y < len(arr[0]):
                print(f'{i} 방향에있는 수는 {arr[temp_x][temp_y]}')

            else :
                print(f'벽 밖에 있는 수 입니다 : {temp_x}{temp_y}')






# 상하좌우
dx = [1,-1,0,0]
dy = [0,0,-1,1]