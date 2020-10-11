# 3. 조작 점수 제거

k = int(input())
# score = list(map(int, input().split()))
# score = [24,22,20,10,5,3,2,1]
score = [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]
diffs = {}
for i in range(1,len(score)):
  diff = score[i-1]-score[i]
  if diff in diffs.keys():
    diffs[diff] += 1
  else: diffs[diff] = 1

answer = -1
for j in diffs.keys():
   if diffs[j] < k:
     answer += diffs[j]
print(answer)