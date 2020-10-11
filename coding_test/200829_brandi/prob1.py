# 1. 스마트 밴드

import sys

N = int(input())
ans = [0,0,0,0,0,0]
while True:
  try:

    mx = int(input())/(220-N)*100
    if mx < 60: ans[5] += 1
    elif mx < 68: ans[4] += 1
    elif mx < 75: ans[3] += 1
    elif mx < 80: ans[2] += 1
    elif mx < 90: ans[1] += 1
    else: ans[0] += 1

    print(ans)
  except EOFError:
    print(" ".join(str, ans))