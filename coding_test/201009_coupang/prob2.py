# 2. AI은행 키오스크

# n = 3
n = 2
# customers = ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]
customers = ["02/28 23:59:00 03","03/01 00:00:00 02", "03/01 00:05:00 01"]
days = [31,28,31,30,31,30,31,31,30,31,30,31]
kiosk = [0]*n
ans = [0]*n
for i in customers:
  T = int(i[:2])*60*60*24*days[int(i[:2])]+int(i[3:5])*60*60*24+int(i[6:8])*60*60+int(i[9:11])*60+int(i[12:14])
  t = int(i[15:])*60
  # find
  find = False
  for k in range(len(kiosk)):
    if kiosk[k] < T and kiosk[k] == min(kiosk):
      kiosk[k] = T+t
      ans[k] += 1
      find = True
      break
  if not find:
    k = kiosk.index(min(kiosk))
    kiosk[k] += t
    ans[k] += 1
print(max(ans))