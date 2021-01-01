# 꽃집
# 시간 초과

def f(k,cur,price):
    global ans
    if k==K-1:
        price += (sum(prices[cur:]))*(N-cur)
        if ans > price: ans = price
        return
    for i in range(cur+1,N-K+k+2):
        f(k+1,i,price+(sum(prices[cur:i]))*(i-cur))

N,K = map(int,input().split())
prices = list(map(int,input().split()))
ans = 2500000000
f(0,0,0)
print(ans)