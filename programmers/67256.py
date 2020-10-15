# [카카오 인턴] 키패드 누르기
# 2020 카카오 인턴십

num = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2), 0:(3,1)}
def solution(numbers, hand):
    answer = []
    left,right = (3,0),(3,2)
    for n in numbers:
        r,c = num[n][0],num[n][1]
        l_diff,r_diff = abs(left[0]-r)+abs(left[1]-c),abs(right[0]-r)+abs(right[1]-c)
        if n in (3,6,9) or n in (2,5,8,0) and (l_diff > r_diff or l_diff==r_diff and hand=='right'):
            right = (r,c)
            answer.append('R')
        else:
            left = (r,c)
            answer.append('L')
    return "".join(answer)

print(solution([1,3,4,5,8,2,1,4,5,9,5],"right")) # "LRLLLRLLRRL"
print(solution([7,0,8,2,8,3,1,5,7,6,2],"left")) # "LRLLRRLLLRR"
print(solution([1,2,3,4,5,6,7,8,9,0],"right")) # "LLRLLRLLRL"