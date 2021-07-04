answer = 0

def solution(triangle):
    global end
    end = len(triangle)
    start_node = triangle[0][0]
    new_val = [[] for _ in range(end)]
    # 최대합을 저장할 2차원 리스트
    new_val[0].append(start_node)

    for i in range(end):
        for j in range(len(triangle[i])):
            curr = triangle[i][j]

			# 맨 윗줄이면 그냥 넘어간다.
            if i == 0:
                continue
            # 대각선 위로 2개가 존재하는 경우 둘중에 더 큰값을 더한다.
            if j > 0 and j < len(triangle[i])-1:
                val = max(new_val[i-1][j-1], new_val[i-1][j])
                curr += val
            # 오른쪽 위 대각선만 존재하는 경우
            elif j == 0:
                curr += new_val[i-1][j]
            # 왼쪽 위 대각선만 존재하는 경우
            elif j == len(triangle[i])-1:
                curr += new_val[i-1][j-1]

			# 구한 현재까지 최대합을 저장한다.
            new_val[i].append(curr)

	# 최종적으로 맨 마지막줄에서 최댓값이 구할수있는 최대합이다.
    return max(new_val[-1])