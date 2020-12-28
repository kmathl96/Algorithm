# 스킬트리
# Summer/Winter Coding(~2018)

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        flag = True
        for j in range(len(skill)-1,-1,-1):
            if skill[j] not in tree: continue
            idx = tree.index(skill[j])
            for i in range(j):
                if skill[i] not in tree[:idx]:
                    flag = False
                    break
            if not flag: break
        if flag: answer += 1
    return answer

print(solution("CBD",["BACDE","CBADF","AECB","BDA"])) # 2