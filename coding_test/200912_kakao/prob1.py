def solution(new_id):
    new_id = new_id.lower()
    tmp = ''
    for i in range(len(new_id)):
        if new_id[i] in '1234567890qwertyuiopasdfghjklzxcvbnm-_.':
            if i > 0 and len(tmp) > 0 and tmp[-1] == '.' and new_id[i] == '.':
                continue
            tmp += new_id[i]
    if len(tmp) > 0 and tmp[0] == '.': tmp = tmp[1:]
    if len(tmp) > 0 and tmp[-1] == '.': tmp = tmp[:-1]
    if len(tmp) == 0: tmp = 'a'
    if len(tmp) > 15: tmp = tmp[:15]
    if len(tmp) > 0 and tmp[-1] == '.': tmp = tmp[:-1]
    if len(tmp) < 3: tmp += tmp[-1]*(3-len(tmp))
    return tmp