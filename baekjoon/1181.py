# 단어 정렬
# 문자열, 정렬

import sys
input = sys.stdin.readline

N = int(input()) # 단어의 개수
words = list(set([input() for _ in range(N)])) # 단어 리스트
print(''.join(sorted(words,key=lambda x: (len(x),x)))) # 길이 순, 사전 순으로 정렬