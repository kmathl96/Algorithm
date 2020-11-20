# 모의고사
# 완전탐색

def solution(answers):
    answer = []
    a,b,c = [1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]
    ans = [0,0,0]
    for i in range(len(answers)):
        if a[i%5]==answers[i]: ans[0]+=1
        if b[i%8]==answers[i]: ans[1]+=1
        if c[i%10]==answers[i]: ans[2]+=1
    for i in range(3):
        if ans[i]==max(ans): answer.append(i+1)
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))