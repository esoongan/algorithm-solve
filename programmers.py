def solution(n, build_frame):
    answer = []

    graph = [[[False, False] for _ in range(n+1)] for _ in range(n+1)]
    print(graph[0][0])

    for i in build_frame:
        a,b,thing,do = i[0],i[1],i[2],i[3]
        # 0- 삭제, 1- 설치
        # 기둥일때
        if thing == 0:
            # 기둥 - 설치
            if do == 1:
                if check_gidung(a,b, graph):
                    graph[a][b][0] = True
                else:
                    continue
            # 기둥 - 삭제
            elif do == 0:
                if check_remove_gidung(a,b,graph):
                    graph[a][b][0] = False
                else:
                    continue


        # 보일때
        elif thing == 1:
            # 보 - 설치
            if do == 1:
                if check_bo(a,b, graph):
                    graph[a][b][1] = True
                else:
                    continue
            #보 - 삭제
            elif do == 0:
                if check_remove_bo(a,b,graph):
                    graph[a][b][1] = False
                else:
                    continue

    # print(graph[0])
    # print(graph[1])
    # print(graph[2])
    # print(graph[3])
    # print(graph[4])
    # print(graph[5])


    for i in range(n+1):
        for j in range(n+1):
            gidung, bo = graph[i][j][0], graph[i][j][1]
            if gidung:
                answer.append([i,j,0])
            if bo:
                answer.append([i,j,1])

    print(answer)
    return answer

# a,b위치에 기둥을 세울수 있는가?
def check_gidung(a,b, graph):
    if b == 0:
        return True
    # 좌표 (a-1,b)위치의 기둥(0)이 세워져있다면
    elif graph[a][b-1][0] == True:
        return True
    elif graph[a-1][b][1] == True or graph[a][b][1] == True:
        return True
    else:
        return False

# a,b에 보를 세울수 있냐?
def check_bo(a,b, graph):
    # 밑에 기둥있는경우
    if graph[a][b-1][0] == True or graph[a+1][b-1][0]:
        return True
    elif graph[a-1][b][1] == True or graph[a+1][b][1] == True:
        return True
    else:
        return False

def check_remove_gidung(a,b,graph):
    # 임의로 삭제를 해본다.
    # 삭제한후에 영향을 받는 좌표들을 기점으로 설치가 가능한지 확인한다.
    # 설치가 가능하다면 삭제가 가능하다.

    temp = graph.copy()
    temp[a][b][0] = False
    temp[a-1][b+1][1] = False
    temp[a][b+1][1] = False
    temp[a][b+1][0] = False

    # 영향받는 좌표 - 보(a-1, b+1), 보(a, b+1), 기둥(a,b+1)
    if check_bo(a-1, b+1, temp):
        if check_bo(a, b+1, temp):
            if check_gidung(a, b+1, temp):
                return True
    return False


def check_remove_bo(a,b, graph):
    # 임의로 삭제를 해본다.
    # 삭제한후에 영향을 받는 좌표들을 기점으로 설치가 가능한지 확인한다.
    # 설치가 가능하다면 삭제가 가능하다.

    temp = graph.copy()
    temp[a-1][b][1] = False
    temp[a+1][b][1] = False
    temp[a][b][0]= False
    temp[a+1][b][0] = False

    # 영향받는 좌표 - 보(a-1, b) (a+1, b), 기둥 (a,b), (a+1, b)

    if check_bo(a-1, b, temp):
        if check_bo(a+1, b, temp):
            if check_gidung(a, b, temp):
                if check_gidung(a+1,b,temp):
                    return True
    return False
