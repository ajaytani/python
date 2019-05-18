""" Given a smaller string 5 and a bigger string b,
design an algorithm to find all permutations of the shorter string within
the longer one. Print the location of each permutation."""
# aaddcsaadedsaaddaacas
import itertools


def check_perm(B,C):
    print(B,C)
    if len(B) != len(C):
        return False
    elif set(B) == set(C):
        return True
dict = {}
def get_perm(B):
    out =[]
    if B in dict:
        return dict[B]
    elif len(B) ==1:
        dict[B] = B
    else:
        dict[B] = []
        for i, let in enumerate(B):
            print ("B[:i]:{}  + B[i + 1:]: {}".format(B[:i],B[i + 1:]))
            for perm in get_perm(B[:i] + B[i + 1:]):
                dict[B].extend([let+perm])
    print(len(dict))
    return set(dict[B])

def string_perm(A,B):
    b =len(B)
    i =0
    l =len(A)
    lst =[]
    while i <l:
        if A[i] in B:
            #check if A[i:i+b] is a permutation of B
            if (i+b <l):
                if check_perm(A[i:i+b],B):
                    lst.append(i)
                    i+=1
                else:
                    i +=1
            else:
                break
        else:
            i +=1

    return lst

# print(string_perm('abccabbcadasc','abc'))
print(get_perm('aabc'))

print (["".join(x) for x in itertools.permutations('abc')])