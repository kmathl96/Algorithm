# 연도 진행바

month, dd, yyyy, time = input().split()
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m_idx = months.index(month)
dd = int(dd[:-1])
yyyy = int(yyyy)
day = sum(days[:m_idx])+dd-1
year = 365
if not yyyy%400 or not yyyy%4 and yyyy%100:
    year += 1
    if m_idx>1: day += 1
total = year*24*60
print((day*24*60 + int(time[:2])*60 + int(time[3:]))*100/total)