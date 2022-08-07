"""
포켓몬
https://school.programmers.co.kr/learn/courses/30/lessons/1845

"""


def solution(nums):
    s = len(nums) // 2
    k = len(set(nums))
    answer = s if k >= s else k
    return answer


