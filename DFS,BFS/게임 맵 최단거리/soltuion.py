from heapq import heappush,heappop
#BFS 넓이 우선 탐색
#created 2023/05/19 
def solution(maps):
    # row_map, col_map 범위 선언
    row_map , col_map = len(maps),len(maps[0])
    # queue 변수 선언
    QUEUE = []
    # QUEUE에 초기값 넣기 [1,0,0] 위치에 주어진 값,행,열
    heappush(QUEUE,(maps[0][0],0,0))
    # test
    # print(QUEUE)
    
    while QUEUE:
        #유저 값,행,열 선언
        u_value,u_row,u_col = heappop(QUEUE)
        #이동 할 수 있는 곳이 있는지 12~9시 시계방향으로 반복 
        for move_row,move_col in (-1,0),(0,1),(1,0),(0,-1):
            # 유저가 상하좌우로 이동한 좌표 선언
            new_row,new_col = u_row+move_row , u_col+move_col
            # maps 범위안에 있는지 확인
            if new_row in range(row_map) and new_col in range(col_map) and maps[new_row][new_col]:
                # 이동할 위치값이 1인지 확인
                if maps[new_row][new_col] == 1:
                    maps[new_row][new_col] = u_value+1
                    heappush(QUEUE,(maps[new_row][new_col],new_row,new_col))

    return -1 if maps[row_map-1][col_map-1] == 1 else maps[row_map-1][col_map-1]