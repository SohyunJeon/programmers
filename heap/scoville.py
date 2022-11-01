"""
더 맵게
https://school.programmers.co.kr/learn/courses/30/lessons/42626?language=python3

"""



#%% 정확성 O / 효율성 X

scoville = [1, 2, 3]
K = 7


def solution(scoville, K):
    count = 0
    while(True):
        first = min(scoville)
        if first >= K:
            return count
        scoville.remove(first)
        second = min(scoville)
        scoville.remove(second)
        mixed = first + (second * 2)
        count += 1
        scoville.append(mixed)

        if len(scoville) == 1:
            if min(scoville) < K:
                return -1
            else:
                return count


result = solution(scoville, K)





#%%
import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while(scoville[0] < K):
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mixed = first + second * 2
        count += 1
        heapq.heappush(scoville, mixed)

        if len(scoville) == 1:
            if scoville[0] >= K:
                return count
            else:
                return -1
    return count




scoville = [3, 2, 3, 2, 1, 5]
K = 7

result = solution(scoville, K)

