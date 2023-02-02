import heapq

"""
하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온
 작업부터 처리합니다.
"""
# jobs = [[0, 3], [1, 9], [2, 6]]
jobs = [[0, 16], [0, 14], [15, 1], [13, 13]]



heapq.heapify(jobs)
jobs.sort(key=lambda x: sum(x))

wait_list = []
work_sum = 0
for job in jobs:
    wait_time = work_sum - job[0] + job[1]
    work_sum += job[1]

    wait_list.append(wait_time)
result = sum(wait_list)/len(wait_list)



#%% 실패

import heapq

# jobs = [[0, 3], [1, 9], [2, 6]]
jobs = [[0, 16], [0, 14], [15, 1], [13, 13]]

heapq.heapify(jobs)
jobs.sort(key=lambda x: sum(x))
work_sum = 0
pre_finish = 0
for job in jobs:
    work_sum += pre_finish - job[0] + job[1]
    pre_finish += job[1]
result = int(work_sum/len(jobs))


#%% 최종 제출
import heapq



def solution(jobs):
    job_list = []
    start = -1
    now = 0  # 현재시점
    answer = 0
    i = 0

    while (i < len(jobs)):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(job_list, (job[1], job[0]))  # 작업 대기 시간순 정렬

        if job_list:  # 현재 처리하는 작업
            cur_work = heapq.heappop(job_list)  # heap min값 꺼냄
            start = now
            now += cur_work[0]  # 현재 시점 + 현재 처리 할 작업의 소요 시간 -> 작업이 종료될 절대시간
            answer += (now - cur_work[1])  # 작업 종료 시간 - 작업 요청 시간 = 해당 작업의 요청~종료시간 => 누적
            i += 1
        else:  # 현재 처리할 수 있는 작업이 없다면
            now += 1  # 시간 1ms 추가

    return answer // i


jobs = [[0, 16], [0, 14], [15, 1], [13, 13]]
result = solution(jobs)

