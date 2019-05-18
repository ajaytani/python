def palindrome_permutation(s):
    l = len(s)
    if l <= 1:
        return True
    cnt = {}
    check = False
    for i in s:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    for i in cnt:
        if cnt[i] % 2 == 1 and i != ' ':
            if check:
                return False
            check = True
    return True
print(palindrome_permutation('aassddffgghhjjkkll qqwweerrttyyuuiiooppzzxxccvvbbnnmmx'))