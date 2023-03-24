"""
올바른 괄호
https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3
"""

def solution(s):
    if s[0] == ")":
        return False

    checks = []
    for c in list(s):
        if c == "(":
            checks.append(c)
        else:
            checks.pop() if checks else None
    answer = True if len(checks) == 0 else False
    return answer


case = ")()("
print(solution(case))


