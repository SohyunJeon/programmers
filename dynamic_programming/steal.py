"""
https://school.programmers.co.kr/learn/courses/30/lessons/42897?language=python3
"""


def solution(money: list)-> int:
    m_1 = [money[0], money[0]]
    m_2 = [0, money[1]]
    for i in range(2, len(money)-1):
        m_1.append(max(m_1[i-1], money[i]+m_1[i-2]))
    for i in range(2, len(money)):
        m_2.append(max(m_2[i-1], money[i]+m_2[i-2]))
    answer = max(max(m_1), max(m_2))
    return answer

if __name__ == '__main__':
    money = [1, 2, 3, 4]
    result = solution(money)