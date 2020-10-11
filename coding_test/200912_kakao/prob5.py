# 5. 죠르디의 공익광고

def toTime(s):
    return int(s[:2])*60*60+int(s[3:5])*60+int(s[6:])

def toStr(t):
    h = t//3600
    m = t%3600//60
    s = t%60
    return format(h,'02') + ':' + format(m,'02') + ':' + format(s,'02')

def solution(play_time, adv_time, logs):
    mx = 0
    answer = 0
    time = [0]*toTime(play_time)
    for log in logs:
        for i in range(toTime(log[:8]), toTime(log[9:])):
            time[i] += 1
    for i in range(toTime(play_time)-toTime(adv_time)):
        tmp = sum(time[i:i+toTime(adv_time)])
        if mx < tmp:
            mx = tmp
            answer = i
    return toStr(answer)