# 4. 배송 경로

depar = "SEOUL"
hub = "DAEGU"
dest = "YEOSU"
roads = [["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]]
# depar = "ULSAN"
# hub = "SEOUL"
# dest = "BUSAN"
# roads = [["SEOUL","DAEJEON"],["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","ULSAN"],["DAEJEON","BUSAN"],["GWANGJU","BUSAN"]]
def solution(depar, hub, dest, roads):
  answer = 0
  st = [(depar, 0)]
  while st:
    now = st.pop()
    for road in roads:
      if now[0] == road[0]:
        if road[1] == dest:
          if now[1]: answer += 1
        elif now[1] or road[1] == hub:
          st.append((road[1], 1))
        else: st.append((road[1], 0))
  return answer%10007

print(solution(depar, hub, dest, roads))