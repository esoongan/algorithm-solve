# 교집합의 크기 /합집합의 크기
# 집합 a,b가 공집합일땐 1로 정의
# 다중집합의 경우 교집합은 min, 합집합은 max
import re
def solution(str1, str2):
    # 1. 대문사-> 소문자로
    str1 = str1.lower()
    str2 = str2.lower()

    # 2. 2글자씩 끊어서 리스트로 만든다.
    temp1_list = []
    temp2_list = []
    for i in range(0, len(str1)-1):
        temp1_list.append(str1[i:i+2])
    for i in range(0, len(str2)-1):
        temp2_list.append(str2[i:i+2])

    str1_list = []
    str2_list = []
    # 3. 알파벳만 남긴다 by 정규식
    for i in temp1_list:
        i = re.sub(r'[^a-z]', '', i)
        if len(i) !=2:
            continue
        str1_list.append(i)
    for i in temp2_list:
        i = re.sub(r'[^a-z]', '', i)
        if len(i) != 2:
            continue
        str2_list.append(i)

    if len(str2_list) == 0 and len(str2_list) == 0:
        return 1

    #print(str1_list)
    #print(str2_list)

    # 4. Counter를 이용해서 중복되는 원소들의 개수를 찾는다.
    from collections import Counter
    count1 = Counter(str1_list)
    count2 = Counter(str2_list)

    # 5. 1차적으로 각각을 집합으로 바꾼다음 교집합의 대상이될 원소들을 찾는다.

    set1 = set(str1_list)
    set2 = set(str2_list)



    oneandtwo = set1 & set2
    oneortwo = set1 | set2

    # {1,2} -> 교집합의 개수는 min(1에서 1의개수, 2에서 1의개수), min(1에서2의개수, 2에서 2의개수)
    # 합집합의 원소들을 찾는다.

    resultOfAnd = 0 # 교집합의 개수
    for i in list(oneandtwo):
        resultOfAnd += min(count1[i], count2[i])

    # {1,2} -> max로 개수구하기
    # 1에서 교집합의 대상들을  뺀 갯수
    # 2에서도 교집합의 대상들을 뺀 갯수 ,,,이 3가지 경우를 모두 더한것
    resultOfOr = 0
    for i in list(oneandtwo):
        resultOfOr += max(count1[i], count2[i])
        count1.pop(i)
        count2.pop(i)

    resultOfOr += sum(count1.values())
    resultOfOr += sum(count2.values())


    #print(resultOfAnd)
    #print(resultOfOr)

    if resultOfOr == 0 :
        return 1

    return int((resultOfAnd / resultOfOr) * 65536)

k = solution('aa1+aa2', 'AAAA12')
print(k)