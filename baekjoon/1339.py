# 단어 수학
# 그리디, 브루트포스

N = int(input()) # 단어의 개수

# 각 알파벳의 자릿수를 더하기
# ex) 첫 번째 단어가 "GCF"이면, arr = [0,0,10,0,0,1,100,...]
#     두 번째 단어가 "ACDEB"이면, arr = [10000,1,1010,100,10,1,100,...]
arr = [0]*26

for _ in range(N):
    word = input() # 단어
    M = len(word)
    for i in range(M):
        # 각 알파벳의 자릿수에 맞춰서 값 갱신
        arr[ord(word[i])-65] += 10**(M-1-i)

# 높은 자릿수를 갖는 알파벳을 큰 수로 바꾸면, 수의 합이 최대가 됨
ans,num = 0,9 # 수의 합, 해당 알파벳을 바꿀 숫자
for a in sorted(arr,reverse=1): # 내림차순 정렬
    if not a: break # 0이면 종료 (그 뒤도 0 => 더 반복할 필요 없음)
    ans += a*num # 자릿수에 숫자를 곱해 더함
    num -= 1 # 숫자 1 감소
print(ans)