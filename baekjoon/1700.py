# 멀티탭 스케줄링
# 그리디

N,K = map(int,input().split()) # 멀티탭 구멍의 개수, 전기 용품의 총 사용횟수
plugs = list(map(int,input().split())) # 전기용품의 이름
tap = [] # 멀티탭에 꽂아져있는 전기용품
cnt = 0 # 플러그를 빼는 최소의 횟수

# 전기용품을 사용한 순서대로 확인
for i in range(K):
    # i) 이미 해당 전기용품의 플러그가 멀티탭에 꽂아져있는 경우
    if plugs[i] in tap:
        continue # 플러그를 뺄 필요가 없으므로 넘어감
    
    # ii) 멀티탭에 아직 플러그가 다 꽂아져있지 않은 경우
    if len(tap)<N:
        # 해당 전기용품의 플러그를 꽂음
        tap.append(plugs[i])
        continue
    
    # iii) 멀티탭이 가득 차있으면서 해당 전기용품의 플러그는 없는 경우
    # 다른 전기용품의 플러그를 빼고 꽂아야 함 => 뺄 플러그 찾기
    remove_idx,remove_plug = 0,0 # 뺄 플러그의 인덱스 값과 이름
    remain = plugs[i:] # 남아있는 전기용품

    # 멀티탭에 꽂아져있는 전기용품 확인
    for plug in tap:
        # 더 이상 사용하지 않는 전기용품인 경우
        if plug not in remain:
            remove_plug = plug # 해당 플러그를 뺌
            break # 다른 플러그를 더 확인할 필요가 없으므로 종료
        
        # 멀티탭에 꽂아져있는 플러그 중 제일 나중에 사용하는 전기용품의 플러그를 빼기
        idx = remain.index(plug) # 다음에 해당 전기용품을 사용할 순서

        # 빼려고 했던 전기용품보다 더 나중에 사용하는 경우, 해당 전기용품의 플러그를 뺌
        if remove_idx < idx:
            remove_idx = idx
            remove_plug = plug
    
    # 멀티탭에서 플러그를 빼고 이번에 사용하는 전기용품의 플러그를 꽂음
    tap[tap.index(remove_plug)] = plugs[i]
    cnt += 1 # 플러그 빼는 횟수 증가

print(cnt)