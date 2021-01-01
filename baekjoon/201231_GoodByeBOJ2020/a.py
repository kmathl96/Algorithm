# 끝말잇기

N = int(input())
words = list(input().split())
ans = 1
s = words[0][0]
for w in words:
    if w[0]!=s or w[-1]!=s:
        ans = 0
        break
print(ans)