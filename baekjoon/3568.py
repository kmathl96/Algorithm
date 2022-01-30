# iSharp
# 문자열, 파싱

arr = list(input().split()) # 변수 선언문

# 변수를 차례대로 탐색
for i in range(1,len(arr)):
    type_ = [] # 추가적인 변수형

    # 변수 선언 마지막 문자(`,`나 `;`)를 제외하고, 마지막부터 거꾸로 탐색
    for j in range(len(arr[i])-2,-1,-1):
        # 배열의 여는 괄호는 닫힌 괄호 때 같이 붙여줄 것이므로 넘어감
        if arr[i][j] == '[': continue
        # 배열의 닫힌 괄호는 여는 괄호와 함께 붙여줌
        elif arr[i][j] == ']':
            type_.append('[' + arr[i][j])
        # 참조나 포인터의 경우, 그냥 붙임
        elif arr[i][j] in '*&':
            type_.append(arr[i][j])
        # 배열, 참조, 포인터가 아닌 경우, 변수 이름이므로 종료
        else: break

    # 기본 변수형 + 추가 변수형 + 변수의 이름
    print(f'{arr[i][0]}{"".join(type_)} {arr[i][:j+1]};')