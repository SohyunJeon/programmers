#%%
"""
신규 아이디 추천
https://school.programmers.co.kr/learn/courses/30/lessons/72410

"""
import re

def solution(new_id):
    valid_pass = True
    # 아이디의 길이는 3자 이상 15자 이하여야 합니다.
    valid_pass = True if (len(new_id) >= 3) and (len(new_id) <= 15) else False
    # 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
    if valid_pass:
        p1 = re.compile(r'[a-z0-9\_\-\.]+')
        v1 = re.fullmatch(p1, new_id)
        if v1 == None:
            valid_pass = False
        else:
            valid_pass = False if v1.string != new_id else True

    # 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
    if valid_pass:
        p2 = re.compile(r'(^\.)+|(\.\.)+|(\.)$')
        v2 = re.search(p2, new_id)
        if v2 != None:
            valid_pass = False

    if valid_pass:
        return new_id
    ## 제안
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    mod_id1 = new_id.lower()

    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    mod_id2 = re.sub(r'[^a-z0-9\-\_\.]', '', mod_id1)

    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    mod_id3 = re.sub(r'(\.)+', '.', mod_id2)

    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    mod_id4 = re.sub(r'^(\.)|(\.)$', '', mod_id3)

    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    new_id5 = 'a' if mod_id4 == '' else mod_id4

    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    mod_id6 = new_id5[:15]
    mod_id6 = re.sub(r'(\.)$', '', mod_id6)

    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(mod_id6) <= 2:
        final_mod_id = mod_id6 + (mod_id6[-1] * (3-len(mod_id6)))
    else:
        final_mod_id = mod_id6
    return final_mod_id

