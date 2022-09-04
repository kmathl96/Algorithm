# 숫자 게임
# 구현, 브루트포스

from itertools import combinations

N = int(input()) # 사람의 수
cards = [list(map(int,input().split())) for _ in range(N)] # 각 사람이 가진 카드

# 1) 세 장의 카드를 선택할 때 그 합의 일의 자리 수가 가장 큰 사람을 찾아야 함
#    => 각 사람에 대해, 만들 수 있는 숫자 합을 조합으로 구한 후 최댓값을 저장
# 2) 가장 큰 수를 갖는 사람이 두 명 이상일 경우, 번호가 가장 큰 사람의 번호를 출력
#    => 뒷사람부터 카드를 선택하여 저장
sums = [max(sum(nums)%10 for nums in combinations(cards[i],3)) for i in range(N-1,-1,-1)]
print(N-sums.index(max(sums)))