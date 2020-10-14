# 시저 암호

def solution(s, n):
    answer = []
    for i in s:
        if i in ' ': answer += ' '
        elif ord(i)<97:
            answer.append(chr((ord(i)-65+n)%26+65))
        else: answer.append(chr((ord(i)-97+n)%26+97))
    return ''.join(answer)

print(solution('AB',1)) # 'BC'
print(solution('z',1)) # 'a'
print(solution('a B z',4)) # 'e F d'
print(solution('AaZz',25)) # 'ZzYy'