# 일곱 난쟁이
# 기초 - 브루트 포스

num = [int(input()) for _ in range(9)]
total = sum(num) # 총합
flag = False # 경우를 찾았는지 여부 판단
for i in range(8):
    for j in range(i+1,9):
        if total-num[i]-num[j]==100: # 두 난쟁이의 키를 총합에서 빼서 확인
            flag = True
            break
    if flag: break
num.pop(j)
num.pop(i)
for n in sorted(num): # 정렬하여 출력
    print(n)