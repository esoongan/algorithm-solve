
rotate_list = []

def clock_rotation(key, depth):

    if depth == 3:
        return

    m = len(key)

    new_key = [[0] * m for _ in range(m)]

    # 시계방향으로 회전
    for i in range(m):
        for j in range(m):
            new_key[j][m-1-i] = key[i][j]

    rotate_list.append(new_key)
    return clock_rotation(new_key, depth+1)


def solution(key, lock):

    # 회전한 키들을 담는 리스트 rotation_list
    rotate_list.append(key)
    clock_rotation(key, 0)

    m = len(key)
    n = len(lock)
    new_n = (3*n)-2

    # 크기를 키운 새로운 lock배열
    new_lock = [[0] * new_n for _ in range(new_n)]

    # new_lock의 중앙에 기존 lock배열을 위치시킨다.
    for i in range(n):
        for j in range(n):
            new_lock[i+n-1][j+n-1] = lock[i][j]

    # 회전한 키에 대해서
    for round in rotate_list:
        for i in range(new_n-m):
            for j in range(new_n-m):
                attach_key(i,j,m,round,new_lock)
                if check(new_lock, n):
                    return True
                dettach_key(i,j,m,round,new_lock)
    return False


# 좌측상단 꼭지점이 x,y일때 키를 붙이는 함수
def attach_key(x,y, m, key, new_lock):
    for i in range(m):
        for j in range(m):
            new_lock[x+i][y+j] += key[i][j]

def dettach_key(x,y,m,key,new_lock):
    for i in range(m):
        for j in range(m):
            new_lock[x+i][y+j] -= key[i][j]

# 자물쇠가 풀렸나?
def check(new_lock, n):
    middle = get_middle(new_lock, n)
    print(middle)
    for line in middle:
        for i in line:
            if i != 1: # 홈이 남아있다.
                return False
    return True

def get_middle(new_lock, n):
    middle = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            middle[i][j] = new_lock[i+n-1][j+n-1]
    return middle

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1, 0], [1, 1, 0,0], [1, 0, 1,0],[1, 0, 1,0]]
print(solution(key, lock))