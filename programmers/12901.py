# 2016년

m = [31,29,31,30,31,30,31,31,30,31,30,31]
w = ['SUN','MON','TUE','WED','THU','FRI','SAT']

def solution(a, b):
    return w[(sum(m[:a-1])+b+4)%7]

print(solution(1,1)) # "FRI"
print(solution(5,24)) # "TUE"