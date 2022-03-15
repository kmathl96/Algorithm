# 카드게임
# 구현

# 점수 정하기
def f():
    cond = [0]*10 # 각 규칙을 만족하는지 여부
    
    # 카드 5장이 모두 같은 색인지 확인 => 규칙 4 만족
    for k in colors.keys():
        if len(colors[k])==5:
            cond[4] = max(colors[k]) # 가장 높은 숫자 저장
            break
    
    # 카드 5장의 숫자가 연속적인지 확인 => 규칙 5 만족
    cnt = 0
    for i in range(1,6):
        if not nums[i:i+5].count(0):
            cond[5] = i+4 # 가장 높은 숫자 저장
            break
    # 규칙 4와 5를 동시에 만족 => 규칙 1 만족
    if cond[4] and cond[5]:
        # 가장 높은 점수이므로 더 확인할 필요 없음
        return 900 + cond[4] # 점수를 반환하고 종료

    # 숫자가 같은 카드들의 개수 확인
    for i in range(1,10):
        # 4장의 숫자가 같음 => 규칙 2 만족
        if nums[i]==4:
            return 800 + i # 더 확인할 필요가 없으므로 종료
        
        # 3장의 숫자가 같음 => 규칙 6 만족
        if nums[i]==3:
            # 규칙 8(2장의 숫자가 같음)을 동시에 만족 => 규칙 3 만족
            if cond[8]:
                # 점수(700 + 3장이 같은 숫자(i)*10 + 2장이 같은 숫자(cond[8]))를 반환하고 종료
                return 700 + i*10 + cond[8]
            cond[6] = i # 해당 숫자 저장
        
        # 2장의 숫자가 같음 => 규칙 8 만족
        if nums[i]==2:
            # 규칙 6(3장의 숫자가 같음)을 동시에 만족 => 규칙 3 만족
            if cond[6]:
                # 점수(700 + 3장이 같은 숫자(cond[6])*10 + 2장이 같은 숫자(i))를 반환하고 종료
                return 700 + cond[6]*10 + i
            # 이미 규칙 8(2장의 숫자가 같음)을 만족 => 규칙 7 만족
            if cond[8]:
                # 큰 숫자*10 + 작은 숫자 저장
                cond[7] = cond[8]*10 + i if cond[8]>i else i*10 + cond[8]
            # 아직 규칙 8을 만족하지 않는 경우
            else:
                cond[8] = i # 해당 숫자 저장
    
    # 위의 어떤 경우에도 해당하지 않을 때 규칙 9에 따라 가장 큰 숫자 찾기
    for i in range(9,0,-1): # 큰 숫자부터 확인
        # 카드가 있는 경우, 숫자를 저장하고 종료
        if nums[i]:
            cond[9] = i
            break
    
    # 가장 높은 점수 반환
    # 규칙 1~3을 만족하는 경우는 앞에서 먼저 반환했으므로 4부터 확인
    for i in range(4,10):
        if cond[i]:
            return 1000-100*i + cond[i]

colors = {color:[] for color in 'RBYG'} # 색깔별 카드 숫자
nums = [0]*10 # 각 숫자의 카드 개수

# 카드 5장의 정보 저장
for _ in range(5):
    color,num = input().split() # 카드의 색깔과 숫자
    num = int(num)
    colors[color].append(num)
    nums[num] += 1
print(f())