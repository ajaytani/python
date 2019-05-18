def isSubstring(a,b):
    pass
def string_rotation(s1,s2):
    len = len(s1)
    if len == len(s2) and len > 0:
        s1s2 = s1 + s2
        return isSubstring(s1s2,s2)
    return False