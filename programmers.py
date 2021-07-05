# 연산자의 우선순위를 재정의하여 만들수있는 절댓값이 가장 큰 숫자 
# 주어지는 숫자는 모두 양수 
from itertools import permutations
from collections import deque


def solution(expression):
    answer= 0
    # 0. 숫자와 연산자로 분리
    number = ''
    op = set()
    stack = deque([])
    for i in expression:
        if i.isdigit():
            number += i
        else:
            stack.append(number)
            stack.append(i)
            op.add(i)
            number = ''
    stack.append(number)

    # 1. 주어진 문자열에 수식이 몇개있는지 확인
    len_op = len(op)
    op = list(op)
    # 2. 수식의 가능한 우선순위를 모두 구한다.
    for case in permutations(op, len_op):

        # 3. 해당 우선순위대로 계산했을때 나온 값들을 이전계산값과 비교하여 더큰값으로 계쏙 저장한다.
        new_q = deque([])
        temp_stack = stack.copy()
        for i in range(len_op):
            while temp_stack:
                curr = temp_stack.popleft()
                # 현재 우선순위에 해당하는 연산자라면 
                if curr == case[i]:
                    before = new_q.pop()
                    after = temp_stack.popleft()
                    value = str(eval(before + case[i] + after))
                    new_q.append(value)
                else:
                    new_q.append(curr)
            if len(new_q) == 1:
                answer = max(answer, abs(int(new_q[-1])))
            temp_stack = new_q.copy()
            new_q = deque([])
    print(answer)
    return answer

solution("100-200*300-500+20")