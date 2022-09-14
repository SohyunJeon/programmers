"""
기능개발
https://school.programmers.co.kr/learn/courses/30/lessons/42586
"""
import math

def solution(progress, speeds):
    remain = [math.ceil((100-p)/s) for p, s in zip(progress, speeds)]
    compare = [remain[0]]
    answer = []
    for r in remain[1:]:
        if r <= compare[0]:
            compare.append(r)
        else:
            answer.append(len(compare))
            compare = [r]
    answer.append(len(compare))

    return answer