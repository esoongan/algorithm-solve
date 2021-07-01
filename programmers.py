# 힙 자료구조를 사용한다.
# 한번의 반복마다 
# 1. 힙에서 차례로 2개씩 빼서 새로운 음식을 만들어 힙에 추가한다.
# 2. 최소힙에서 값을하나 뺀것이 이미 스코빌지수를 넘었다면끝낸다.
# 3. 힙에 남은 값이 1개인데, 이 1개가 스코빌지수보다 낮다면 -1을 리턴한다.
import heapq



def solution(s, K):
    heapq.heapify(s)

    depth = 0
    while len(s) > 1:
        depth +=1
        a = heapq.heappop(s)
        b = heapq.heappop(s)

        new = a + (b*2)
        heapq.heappush(s, new)

        min_value = s[0] #팝 하지 않고 가장 작은 항목에 액세스하려면, heap[0]을 사용하십시오.
        if min_value > K:
            return depth
    return -1



s = solution([1, 2, 3, 9, 10, 12], 7)
print(s)