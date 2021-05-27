# N개의 최소공배수
# 두 수의 최소공배수는 두 수의 곱에서 두 수의 최대공약수를 나눈 값
# lcm(a,b) = a * b / gcd(a,b)
# 두 수의 최소공배수를 구하고, 그 수와 다음 수의 최소공배수 구하기 반복

# 최대공약수
def gcd(a,b):
    if a < b: a,b=b,a
    if b==0: return a
    return gcd(b,a%b)

def solution(arr):
    num1 = arr[0] # 최소공배수를 구할 수1
    for i in range(1, len(arr)):
        num2 = arr[i] # 최소공배수를 구할 수2
        lcm = num1*num2 // gcd(num1,num2) # 최대공약수를 활용하여 최소공배수 구함
        num1 = lcm # 수1 갱신
    return lcm

print(solution([2,6,8,14])) # 168
print(solution([1,2,3])) # 6