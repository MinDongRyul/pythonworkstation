n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]

x, y ,dit = map(int, input().split())
d[x][y] = 1

map_table = []
for i in range(n):
    map_table.append(list(map(int ,input().split())))

dx = [1, -1,  0,  0] # 동 서 남 북
dy = [0,  0,  1, -1]

def turn_left():
    global dit
    dit -= 1
    if dit == -1:
        dit = 3

count = 1
turn_time = 0
while True:

    turn_left()
    nx = x + dx[dit]
    ny = y + dy[dit]

    if d[nx][ny] == 0 and map_table[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[dit]
        ny = y - dy[dit]

        if map_table[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)

