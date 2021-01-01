# 일곱 난쟁이
# 기초 - 브루트 포스

num = [int(input()) for _ in range(9)]
total = sum(num)
flag = False
for i in range(8):
    for j in range(i+1,9):
        if total-num[i]-num[j]==100:
            flag = True
            break
    if flag: break
num.pop(j)
num.pop(i)
for n in sorted(num):
    print(n)