def solution(s):
    answer = 0
    result = len(s)
    # 자르는 길이가 1~전체길이의 절반까지 모두탐색
    for length in range(1, len(s)//2+1):
        str_list = []

        for i in range(0,len(s),length):
            str_list.append(s[i:i+length])

        answer = ''
        count = 1

        for j in range(len(str_list)-1):
            # 현재와 다음것이 다르면
            if str_list[j] != str_list[j+1]:
                if count > 1:
                    answer += str(count)
                answer += str_list[j]
                count = 1
            else:
                count += 1
        else:
            if count >1:
                answer += str(count)
            answer += str_list[j+1]
        print(answer)
        result = min(result, len(answer))

    return result

solution('abcabcdede')