# 가장 가까운 세 사람의 심리적 거리
# 브루트포스

# MBTI 유형마다 번호 부여
# 각 자리마다 0과 1로 표시(I,N,F,P가 0 / E,S,T,J가 1)
# ex. ISFJ => 0101 => 5
dic = {'INFP':0,'INFJ':1,'INTP':2,'INTJ':3,'ISFP':4,'ISFJ':5,'ISTP':6,'ISTJ':7,'ENFP':8,'ENFJ':9,'ENTP':10,'ENTJ':11,'ESFP':12,'ESFJ':13,'ESTP':14,'ESTJ':15}

# MBTI의 값을 XOR 했을 때의 값을 이진법으로 나타냈을 때의 1의 개수가 심리적 거리
# (XOR(^) : 각각의 자리의 수를 비교했을 때 다르면 1, 같으면 0)
# ex1. ESFJ XOR ISFJ => 1101 XOR 0101 (=13^5) => 1000 (=8, 거리 1) => diff[8] = 1
# ex2. INTJ XOR ISFJ => 0011 XOR 0101 (=3^5) => 0110 (=6, 거리 2) => diff[6] = 2
diff = [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4]

for _ in range(int(input())):
    N = int(input())
    # MBTI가 비슷할수록 심리적 거리가 가까우므로, 결과를 더 빨리 도출하기 위해 정렬
    mbti = sorted(list(input().split()))

    # 비둘기집의 원리
    # 학생이 33(16*2+1)명 이상인 경우,
    # 아무리 골고루 나와도 한 유형 이상은 3명 이상이므로, 심리적 거리의 최솟값은 0
    if N > 32:
        print(0)
        continue
    
    ans = 12
    for i in range(N-2):
        a = dic[mbti[i]]
        for j in range(i+1,N-1):
            b = dic[mbti[j]]
            # a와 b의 심리적 거리가 현재 최솟값보다 크면 더 계산할 필요가 없음
            if ans <= diff[a^b]: break
            for k in range(j+1,N):
                c = dic[mbti[k]]
                ans = min(ans,diff[a^b]+diff[a^c]+diff[b^c])
    print(ans)