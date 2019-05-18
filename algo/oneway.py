#O(shorter array)
def oneway2(s1,s2):
    ls1 = len(s1)
    ls2 = len(s2)
    if abs(ls1-ls2) >1:
        return False
    if ls2 > ls1:
        s1, s2 = s2, s1
        ls1, ls2 = ls2, ls1
    cnt = {}
    small = 0
    large = 0
    founddifference = False
    while large < ls1 and small <ls2:
        if s1[large] != s2[small]:
            if founddifference:
                return False
            founddifference = True
            if ls1 == ls2:
                small += 1
        else:
            small += 1
        large += 1

    return True


print(oneway2('pall','plll'))


def oneway(s1,s2):
    ls1 = len(s1)
    ls2 = len(s2)
    if abs(ls1-ls2) >1:
        return False
    if ls2 > ls1:
        s1, s2 = s2, s1
        ls1, ls2 = ls2, ls1
    cnt = {}
    c = 0
    for i in s1:
        if i in cnt:
            cnt[i] +=1
        else:
            cnt[i] =1
    for i in s2:
        if i in cnt:
            cnt[i] -=1
        else:
            cnt[i] =1
    for i in cnt.keys():
        if (cnt[i] >0):
            c +=1
    if c >1:
        return False
    return True
