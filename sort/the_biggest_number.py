
"""
가장 큰 수
https://school.programmers.co.kr/learn/courses/30/lessons/42746

"""
from functools import cmp_to_key


def compare(x, y):
    result = int(str(x) + str(y)) - int(str(y) + str(x))
    if result > 0:
        return -1
    elif result == 0:
        return 0
    else:
        return 1


def solution(numbers):
    result = sorted(numbers, key=cmp_to_key(compare))
    answer = ''.join([str(x) for x in result])

    answer = '0' if int(answer) == 0 else answer

    return answer

if __name__ == '__main__':
    numbers = [3, 30, 34, 5, 9]
    result = solution(numbers)