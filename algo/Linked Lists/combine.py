def combine(n,k):
    master = []
    buff = ''
    recursive([x for x in range(1, n+1)], master, k, 0, buff)
    return master

def recursive(S,master,have,curr,buff):
    if have ==0:
        master.append([int(x) for x in buff.split()])
    elif curr <len(S) and have >0:
        recursive(S,master,have-1,curr+1, buff + " " + str(S[curr]))
        recursive(S, master, have, curr+1, buff)

print(combine(4,3))