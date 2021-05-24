# 전화번호 목록
# 해시

def solution(phone_book):
    phone_book.sort() # 정렬하면, 바로 뒤의 전화번호만 확인하면 됨
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]: return False
    return True

print(solution(["119", "97674223", "1195524421"])) # false
print(solution(["123","456","789"])) # true
print(solution(["12","123","1235","567","88"])) # false