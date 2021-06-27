def solution(p):
    # 1번
    if not p:
        return ""

    # 2번
    u,v = seperate(p)

    # 3번
    if isBalanced(u):
        #seperate(v)
        # 3-1
        return u + solution(v) # 이부분을 이해하는것이 어려웠다.
    # 4번
    else:
        # 4-1
        answer = '('
        # 4-2
        answer += solution(v)
        # 4-3
        answer += ')'

        # 4-4
        for i in u[1:-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        # 4-5
        return answer

# 문자열을 u와 v로 분리하는 함수
def seperate(p):
    left_count = 0
    right_count = 0
    for idx, i in enumerate(p):
        if i == '(':
            left_count += 1
        elif i == ')':
            right_count += 1
        # 더이상 나눠질 수 없는 올바른 괄호문자열 찾음
        if left_count == right_count:
            return p[:idx + 1], p[idx + 1:] # u,v


def isBalanced(u):
    stack = []

    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True