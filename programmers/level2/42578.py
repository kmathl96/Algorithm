# 위장
# 해시

def solution(clothes):
    answer = 1
    dic = {} # 종류마다 몇 개의 옷이 있는지 저장
    for c in clothes:
        if c[1] in dic.keys(): # dic에 이미 저장돼있는 종류라면 개수 +1
            dic[c[1]] += 1
        else: dic[c[1]] = 1 # dic에 없는 종류라면 개수 1로 저장
    for k in dic.keys():
        answer *= dic[k]+1 # 해당 종류에서 한 가지를 선택(dic[k]) + 아무 것도 선택하지 않는 경우(1)
    return answer-1 # 아무 종류도 선택 안 하는 경우를 제외

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])) # 5
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])) # 3