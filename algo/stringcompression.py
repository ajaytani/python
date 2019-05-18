def string_compress(s):
    cur_cnt = 0
    i = 0
    l = len(s)
    s2 = ''
    if len(s) <= 2:
        return s
    else:
        while i < l:
            if i < l-1 and s[i] != s[i+1]:
                s2 += s[i]+str(cur_cnt+1)
                cur_cnt = 0
                i += 1
            elif i < l-1 and s[i] ==s[i+1]:
                cur_cnt += 1
                i +=1
            elif i == l-1:
                if s[i-1] ==s[i]:
                    s2 += s[i] + str(cur_cnt+1)
                    i += 1
        if len(s2) > l:
            return s
    return s2
print(string_compress('aabcccccaaa'))