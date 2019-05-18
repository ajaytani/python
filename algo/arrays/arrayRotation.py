



def array_left_rotation(a, ln, movk):
    if movk % ln == 0:
        return a
    else:
        modv = movk % ln
        # initial position i 123456 pos i to pos ln + i - r  6-2
        counter=0
        for idx in range(ln):
            if counter < ln:
                tempswap = idx
                modptr = idx + modv
                tmp = a[idx]
                counter+=1 #outer swap for element at index 0
                while(modptr!=idx):
                    print('{}, {}, {} a[t]: {}, a[tp] {}'.format(a,tempswap,modptr,a[tempswap],a[modptr]))
                    a[tempswap] = a[modptr]
                    tempswap = modptr
                    modptr += modv
                    if (modptr >= ln):
                        modptr -= ln
                    counter+=1
                a[tempswap] = tmp
    return a

a= [1,2,3,4,5,56,576,344,22,2]
k= 3
n= 10
answer = array_left_rotation(a, n, k)
print answer
