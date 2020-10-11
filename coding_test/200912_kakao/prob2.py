# 2. 스카피의 코스요리

from itertools import combinations

def solution(orders, course):
    answer = []
    tmp = {c: {} for c in course}
    mx = {c: 0 for c in course}
    for order in orders:
        order = list(order)
        order.sort()
        for c in course:
            for i in list(combinations(order,c)):
                if i in tmp[c].keys():
                    tmp[c][i] += 1
                else: tmp[c][i] = 1
                if mx[c] < tmp[c][i]: mx[c] = tmp[c][i]
    for c in course:
        for k in tmp[c].keys():
            if mx[c] > 1 and tmp[c][k] == mx[c]: answer.append(''.join(k))
    answer.sort()
    return answer