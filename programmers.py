from collections import Counter
from itertools import combinations

temp = []
# 전체사용자 - user_id, 불량사용자목록 - banned_id
# 가능한 경우의수 (전체에서 해당되는 사용자들을 모두 찾고 조합갯수?)
def solution(user_id, banned_id):
    answer = 0
    one_list = []

    # 예외처리 해주니까 테스트케이스 하나 시간초과나던거 해결했다.
    if len(Counter(banned_id).keys())==1:
        for j in user_id:
            if match(j, banned_id[0]):
                one_list.append(j)

        return len(list(combinations(one_list,len(banned_id))))


    ban_len = len(banned_id)
    match_list = [[] for _ in range(ban_len)]

    for idx, i in enumerate(banned_id):
        for j in user_id:
            if match(j, i):
                match_list[idx].append(j)
    # print(match_list)

    for i in match_list[0]:
        curr = []
        dfs(i, 0, match_list[1:], curr)
    result = set()

    for i in temp:
        i = set(i)
        if len(i) != ban_len:
            continue
        result.add(tuple(sorted(i)))

    return len(result)


# ['frodo', 'crodo'], ['abc123', 'frodoc']]
def dfs(start, depth, graph, curr):
    curr.append(start)

    if depth == len(graph):
        temp.append(curr.copy()) ## 또오오오오오오오오
        return

    for i in graph[depth]:
        dfs(i, depth + 1, graph, curr)
        curr.remove(i)


def match(target, banid):

    if len(target) != len(banid):
        return False
    for idx, i in enumerate(banid):
        if i == '*':
            continue
        else:
            if target[idx] != i:
                return False
    return True


u = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b = ["*****", "*****"]

k = solution(u,b)
print(k)