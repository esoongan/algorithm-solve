from collections import defaultdict
def solution(gems):
    answer = (0,0)
    global start
    start, end = 0, 0
    gems_len = len(gems)
    kinds = len(set(gems))
    curr_min = 100000

    interval_dic = defaultdict(int)

    while end < gems_len:
        interval_dic[gems[end]] += 1
        # print(interval_dic)
        # 모든 종류의 보석을 포함하는 끝점을 찾으면
        if len(interval_dic.keys()) == kinds:
            # 시작, 끝 저장
            if curr_min > end-start:
                curr_min = end-start
                answer = (start, end)
            # print(answer)
            # 시작점을 현재의 끝점까지 이동하면서 여전히 조건을 만족하는 부분을 찾는다.
            for i in range(start, end):
                interval_dic[gems[i]] -= 1
                if not interval_dic[gems[i]]:
                    interval_dic.pop(gems[i])
                # 여전히 모든종류를 포함한다면 start를 계속 증가시킨다.
                if len(interval_dic.keys()) == kinds:
                    if curr_min > end - (i+1):
                        curr_min = (end - (i+1))
                        answer = (i+1, end)
                    start = i+1
                else:
                    interval_dic[gems[i]] += 1
                    break
            end += 1
        else:
            end += 1

    a, b = answer
    return [a + 1, b + 1]


g = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(g))