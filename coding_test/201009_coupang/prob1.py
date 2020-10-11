# 1. 자릿수 곱

mx_k = 0
mx = 0

for k in range(2,10):
  tmp = N
  ans = 1
  while tmp > 0:
    if tmp%k > 0:
      ans*=tmp%k
    tmp = tmp//k
  if mx <= ans:
    mx = ans
    if mx_k < k: mx_k=k
print([mx_k,mx])