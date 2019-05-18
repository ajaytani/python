def anagrams(s):
    n = len(s)

    dic = {}

    for word in s:
        orderedstr = str(sorted(word))

        if orderedstr in dic:
            dic[orderedstr].append(word)
        else:
            dic[orderedstr] = [word]
    res = []
    for key in dic:
        if len(dic[key]) > 1:
            res.append(dic[key])

    for i in res:
        print (i)


anagrams(['rats','star','arts','cie','ice'])