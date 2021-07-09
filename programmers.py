def solution(places):
    answer = []
    graph = []

    for place in places:
        p_list = []
        temp = []
        for line in place:
            temp.append(list(line))
        graph.append(temp)

    for i in graph:
        answer.append(check(i, []))
    # [['P', 'O', 'O', 'O', 'P'], ['O', 'X', 'X', 'O', 'X'], ['O', 'P', 'X', 'P', 'X'], ['O', 'O', 'X', 'O', 'X'], ['P', 'O', 'X', 'X', 'P']]
    return answer


def check(graph, p_list):
    for i in range(5):
        for j in range(5):
            if graph[i][j] == 'P':
                p_list.append((i, j))

    #print(p_list)
    while p_list:
        curr = p_list.pop()
        for i in p_list:
            mht = manhatten(curr, i)
            # 맨해튼거리가 2초과이면
            if mht > 2:
                continue
            # 맨해튼거리가 2 이하이면
            elif mht == 2:
                x1, y1 = curr[0], curr[1]
                x2, y2 = i[0], i[1]
                # 같은 행에 위치한경우
                if x1 == x2:
                    if graph[x1][min(y1, y2) + 1] == 'O':
                        return 0
                        # 같은 열에 위치한경우
                elif y1 == y2:
                    if graph[min(x1, x2) + 1][y1] == 'O':
                        return 0
                # 대각선에 위치한경우
                else:
                    if graph[x1][y1] == 'O':
                        return 0
                    elif graph[x1][y2] == 'O':
                        return 0
                    elif graph[x2][y1] == 'O':
                        return 0
                    elif graph[x2][y2] == 'O':
                        return 0
            else:
                return 0
    return 1


def manhatten(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# 모든 응시자의 위치를 구한다.(a,b)
# 특정 응시자와 나머지 모든 응시자를 비교한다.
# 맨해튼거리가 2초과이면 다음 응시자와 비교한다.
# 맨해튼거리가 2이하이면 조건을 나누어 검색한다.
# 거리가 2라면 두 사람을 꼭지점으로 하는 사각형내의 모든 지점에서 O가 하나라도 있다면 지키지 않은것
# 나머지 모든사람과 검사했는데 ㄱㅊ으면 다음사람으로 넘어간다.
