# 정렬
# 가장 큰 수

def solution(numbers):
    # 각 수를 문자열로 바꾼 후
    # 5번 반복한 값을 기준으로 내림차순 정렬
    # 문자열은 글자 순서, 문자열 길이 순서대로 정렬
    # ex) [3,30,34,5,9]
    #   => ['3','30','34','5','9']
    #   => ['33333','3030303030','3434343434','55555','99999']
    #   => ['99999','55555','3434343434','33333','3030303030']
    #   => ['9','5','34','3','30']
    n = sorted(list(map(str,numbers)), key=lambda x: x*5, reverse=0)

    # 0만 주어졌을 경우 정수형으로 바꾼 후 다시 문자열로 반환
    # ex) [0,0] => ['0','0'] => '00' => 0 => '0'
    return str(int("".join(n)))

# 시간 초과
# def solution(numbers):
#     n = sorted(list(map(str,numbers)), reverse=1) # 우선 내림차순으로 정렬
#     for i in range(len(n)-1):
#         for j in range(i+1,len(n)):
#             # 앞문자와 합친 것과 거꾸로 합친 것을 비교해서 후자가 더 큰 경우 숫자를 서로 바꿈
#             if int(n[j-1]+n[j]) < int(n[j]+n[j-1]):
#                 n[j-1],n[j] = n[j],n[j-1]
#     return str(int("".join(n)))

print(solution([6,10,2])) # "6210"
print(solution([3,30,34,5,9])) # "9534330"

print(solution([0,0,0,0])) # "0"
print(solution([10,0,0,1,2,3,4,5,6,7,8,9,10])) # "987654321101000"
print(solution([412,41])) # 41412
print(solution([303,30])) # 30330
print(solution([12,1213])) # 121312
print(solution([15,151])) # 15151
print(solution([998,9,999])) # 9999998