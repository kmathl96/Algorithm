# 가장 가까운 세 사람의 심리적 거리
# 시간 초과

def f(mbti1, mbti2, mbti3):
    d = 0
    for i in range(4):
        if mbti1[i]!=mbti2[i]: d += 1
        if mbti1[i]!=mbti3[i]: d += 1
        if mbti2[i]!=mbti3[i]: d += 1
    return d

for _ in range(int(input())):
    N = int(input())
    mbti = list(input().split())
    ans = 400000
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                tmp = f(mbti[i],mbti[j],mbti[k])
                if ans > tmp: ans = tmp
    print(ans)